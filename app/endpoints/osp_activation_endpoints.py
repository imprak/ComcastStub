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

router = APIRouter(tags=["OSP Activation APIs"])


# Activate field rpd API
@router.post(
    "/v1/partners/{partnerId}/network/activateFieldRpd", description=DESC_CREATE
)
def create_activate_field_rpd(
    data_in: schemas.ActivateFieldRpdCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create activate field rpd request from {username} "
        f"with partner id {partner_id}"
    )

    data_out = schemas.ActivateFieldRpdInDb(
        **data_in.model_dump(),
        **{"activateFieldRpdId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/activateFieldRpd/{activateFieldRpdId}",
    description=DESC_UPDATE,
)
def update_activate_field_rpd(
    data_in: schemas.ActivateFieldRpdUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    activate_field_rpd_id: str = Path(
        ..., title="activateFieldRpd ID", alias="activateFieldRpdId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update activate field rpd request from {username} with partner "
        f"id {partner_id} and activate field rpd id {activate_field_rpd_id}"
    )

    data_out = schemas.ActivateFieldRpdInDb(
        **data_in.model_dump(),
        **{"activateFieldRpdId": activate_field_rpd_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/activateFieldRpd/{activateFieldRpdId}",
    description=DESC_DELETE,
)
def delete_activate_field_rpd(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    activate_field_rpd_id: str = Path(
        ..., title="activateFieldRpd ID", alias="activateFieldRpdId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete activate field rpd request from {username} with partner "
        f"id {partner_id} and activate field rpd id {activate_field_rpd_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Activate shelf rpd API


@router.post(
    "/v1/partners/{partnerId}/network/activateShelfRpd", description=DESC_CREATE
)
def create_activate_shelf_rpd(
    data_in: schemas.ActivateShelfRpdCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create activate shelf rpd request from {username} "
        f"with partner id {partner_id}"
    )

    data_out = schemas.ActivateShelfRpdInDb(
        **data_in.model_dump(),
        **{"activateShelfRpdId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/activateShelfRpd/{activateShelfRpdId}",
    description=DESC_UPDATE,
)
def update_activate_shelf_rpd(
    data_in: schemas.ActivateShelfRpdUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    activate_shelf_rpd_id: str = Path(
        ..., title="activateShelfRpd ID", alias="activateShelfRpdId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update activate shelf rpd request from {username} with partner "
        f"id {partner_id} and activate shelf rpd id {activate_shelf_rpd_id}"
    )

    data_out = schemas.ActivateShelfRpdInDb(
        **data_in.model_dump(),
        **{"activateShelfRpdId": activate_shelf_rpd_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/activateShelfRpd/{activateShelfRpdId}",
    description=DESC_DELETE,
)
def delete_activate_shelf_rpd(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    activate_shelf_rpd_id: str = Path(
        ..., title="activateShelfRpd ID", alias="activateShelfRpdId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete activate shelf rpd request from {username} with partner "
        f"id {partner_id} and activate shelf rpd id {activate_shelf_rpd_id}"
    )

    return status.HTTP_204_NO_CONTENT
