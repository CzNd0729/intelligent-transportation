from fastapi import APIRouter
from app.api.routes.login import router as login_router
from app.api.routes.private import router as private_router
from app.api.routes.users import router as users_router
from app.api.routes.utils import router as utils_router
from app.api.routes.facerecognition import router as facerecognition_router
from app.api.routes.yolo_predict import router as yolo_predict_router
from app.api.routes.yolo_video import router as yolo_video_router
from app.api.routes.data_analysis.clustering import router as clustering_router
from app.api.routes.data_analysis.statistics import router as statistics_router
from app.api.routes.data_analysis.trajectory import router as trajectory_router
from app.api.routes.logger import router as logger_router
from app.api.routes import alarm_process
api_router = APIRouter()

api_router.include_router(login_router)
api_router.include_router(private_router)
api_router.include_router(users_router)
api_router.include_router(utils_router)
api_router.include_router(facerecognition_router)
api_router.include_router(yolo_predict_router)
api_router.include_router(yolo_video_router)
api_router.include_router(clustering_router)
api_router.include_router(statistics_router)
api_router.include_router(trajectory_router)
api_router.include_router(logger_router)
api_router.include_router(alarm_process.router)
