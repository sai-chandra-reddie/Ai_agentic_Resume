from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models.user import User
from app.schemas.auth import UserCreate, UserResponse, Token
from app.services.security import get_password_hash, verify_password, create_access_token
from app.config import settings
from app.services.otp import generate_otp,verify_otp
from app.schemas.auth import OTPVerification

router = APIRouter()



@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if email exists
    result = await db.execute(select(User).where(User.email == user_in.email))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_in.password)
    new_user = User(email=user_in.email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user

@router.post("/verify-otp")
async def verify_otp_endpoint(data: OTPVerification, db: AsyncSession = Depends(get_db)):
    if not verify_otp(data.email, data.otp):
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_verified = True
    await db.commit()
    return {"message": "Email verified successfully"}

@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db)
):
    # Verify user exists
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalars().first()
    
    # Verify password
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Generate token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
