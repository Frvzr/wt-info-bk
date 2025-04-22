from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from src.repository.references_repo import (CategoryRepository,
                                            GroupRepository,
                                            SourceRepository,
                                            OperationRepository,
                                            DepartmentRepository)
from src.services.references_service import (CategoryService,
                                             GroupService,
                                             SourceService,
                                             OperationServie,
                                             DepartmentService)
from src.schemas.references_schema import (CategorySchema,
                                           GroupSchema,
                                           SourceSchema,
                                           OperationSchema,
                                           DepartmentSchema)
from src.db.database import get_db


router = APIRouter(prefix='/api/v1', tags=['reference'])


@router.get('/categories/', response_model=list[CategorySchema])
async def get_all_categories(db: AsyncSession = Depends(get_db)):
    try:
        repository = CategoryRepository(db)
        service = CategoryService(repository)
        return await service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/groups/', response_model=list[GroupSchema])
async def get_all_groups(db: AsyncSession = Depends(get_db)):
    try:
        repository = GroupRepository(db)
        service = GroupService(repository)
        return await service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/sources/', response_model=list[SourceSchema])
async def get_all_sources(db: AsyncSession = Depends(get_db)):
    try:
        repository = SourceRepository(db)
        service = SourceService(repository)
        return await service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/operations/', response_model=list[OperationSchema])
async def get_all_sources(db: AsyncSession = Depends(get_db)):
    try:
        repository = OperationRepository(db)
        service = OperationServie(repository)
        return await service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/departments/', response_model=list[DepartmentSchema])
async def get_all_sources(db: AsyncSession = Depends(get_db)):
    try:
        repository = DepartmentRepository(db)
        service = DepartmentService(repository)
        return await service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
