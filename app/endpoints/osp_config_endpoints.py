from typing import Optional

from fastapi import Depends, status, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app import log, schemas
from app.deps import security

DESC_CREATE = "Creates the Object that will be sent to comcast for consumption"
DESC_UPDATE = "Updates the Object"
DESC_DELETE = "Deletes the Object"

router = APIRouter(tags=["OSP Config APIs"])


# Remote phy intent API
@router.post(
    "/v1/partners/{partnerId}/network/remotePhyIntent", description=DESC_CREATE
)
def create_remote_phy_intent(
    data_in: schemas.RemotePhyIntentCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create remote phy intent request from {username} with partner "
        f"id {partner_id}"
    )

    data_out = schemas.RemotePhyIntentInDb(
        **data_in.model_dump(),
        **{"remotePhyIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/remotePhyIntent/{remotePhyIntentId}",
    description=DESC_UPDATE,
)
def update_remote_phy_intent(
    data_in: schemas.RemotePhyIntentUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    remote_phy_intent_id: str = Path(
        ..., title="remotePhyIntent ID", alias="remotePhyIntentId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update remote phy intent request from {username} with partner "
        f"id {partner_id} and remote phy intent id {remote_phy_intent_id}"
    )

    data_out = schemas.RemotePhyIntentInDb(
        **data_in.model_dump(),
        **{"remotePhyIntentId": remote_phy_intent_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/remotePhyIntent/{remotePhyIntentId}",
    description=DESC_DELETE,
)
def delete_remote_phy_intent(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    remote_phy_intent_id: str = Path(
        ..., title="remotePhyIntent ID", alias="remotePhyIntentId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete remote phy intent request from {username} with partner "
        f"id {partner_id} and remote phy intent id {remote_phy_intent_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Spectrum recommendation API
@router.post(
    "/v1/partners/{partnerId}/network/spectrumRecommendation", description=DESC_CREATE
)
def create_spectrum_recommendation(
    data_in: schemas.SpectrumRecommendationCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create spectrum recommendation request from {username} "
        f"with partner id {partner_id}"
    )

    data_out = schemas.SpectrumRecommendationInDb(
        **data_in.model_dump(),
        **{"spectrumRecommendationId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/spectrumRecommendation/{spectrumRecommendationId}",
    description=DESC_UPDATE,
)
def update_spectrum_recommendation(
    data_in: schemas.SpectrumRecommendationUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    spectrum_recommendation_id: str = Path(
        ..., title="spectrumRecommendation ID", alias="spectrumRecommendationId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a delete spectrum recommendation request from {username} with partner "
        f"id {partner_id} and spectrum recommendation id {spectrum_recommendation_id}"
    )

    data_out = schemas.SpectrumRecommendationInDb(
        **data_in.model_dump(),
        **{"spectrumRecommendationId": spectrum_recommendation_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/spectrumRecommendation/{spectrumRecommendationId}",
    description=DESC_DELETE,
)
def delete_spectrum_recommendation(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    spectrum_recommendation_id: str = Path(
        ..., title="spectrumRecommendation ID", alias="spectrumRecommendationId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete spectrum recommendation request from {username} with partner "
        f"id {partner_id} and spectrum recommendation id {spectrum_recommendation_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Video configuration API


@router.post(
    "/v1/partners/{partnerId}/network/videoConfiguration", description=DESC_CREATE
)
def create_video_configuration(
    data_in: schemas.VideoConfigurationCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create video configuration request from {username} "
        f"with partner id {partner_id}"
    )

    data_out = schemas.VideoConfigurationInDb(
        **data_in.model_dump(),
        **{"videoConfigurationId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/videoConfiguration/{videoConfigurationId}",
    description=DESC_UPDATE,
)
def update_video_configuration(
    data_in: schemas.VideoConfigurationUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    video_configuration_id: str = Path(
        ..., title="videoConfiguration ID", alias="videoConfigurationId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update video configuration request from {username} with partner "
        f"id {partner_id} and video configuration id {video_configuration_id}"
    )

    data_out = schemas.VideoConfigurationInDb(
        **data_in.model_dump(),
        **{"videoConfigurationId": video_configuration_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/videoConfiguration/{videoConfigurationId}",
    description=DESC_DELETE,
)
def delete_video_configuration(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    video_configuration_id: str = Path(
        ..., title="videoConfiguration ID", alias="videoConfigurationId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete video configuration request from {username} with partner "
        f"id {partner_id} and video configuration id {video_configuration_id}"
    )

    return status.HTTP_204_NO_CONTENT
