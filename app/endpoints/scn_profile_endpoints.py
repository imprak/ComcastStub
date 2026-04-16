from typing import Optional
import uuid

from fastapi import Depends, status, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app import log, schemas
from app.deps import security

DESC_CREATE = "Creates the Object that will be sent to comcast for consumption"
DESC_UPDATE = "Updates the Object"
DESC_DELETE = "Deletes the Object"
router = APIRouter(tags=["SCN Profile APIs"])


# Service class APIs
@router.post("/v1/partners/{partnerId}/network/serviceClass", description=DESC_CREATE)
def create_service_class(
    data_in: schemas.ServiceClassCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create service class request from {username} with partner "
        f"id {partner_id}"
    )

    data_out = schemas.ServiceClassInDb(
        **data_in.model_dump(),
        **{"serviceClassId": str(uuid.uuid4())},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/serviceClass/{serviceClassId}",
    description=DESC_UPDATE,
)
def update_service_class(
    data_in: schemas.ServiceClassUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    service_class_id: str = Path(..., title="serviceClass ID", alias="serviceClassId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update service class request from {username} with partner "
        f"id {partner_id} and service class id {service_class_id}"
    )

    data_out = schemas.ServiceClassInDb(
        **data_in.model_dump(),
        **{"serviceClassId": service_class_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/serviceClass/{serviceClassId}",
    description=DESC_DELETE,
)
def delete_service_class(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    service_class_id: str = Path(..., title="serviceClass ID", alias="serviceClassId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete service class request from {username} with partner "
        f"id {partner_id} and service class id {service_class_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Service class value API
@router.post(
    "/v1/partners/{partnerId}/network/serviceClassValue", description=DESC_CREATE
)
def create_service_class_value(
    data_in: schemas.ServiceClassValueCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create service class value request from {username} with partner "
        f"id {partner_id}"
    )

    data_out = schemas.ServiceClassValueInDb(
        **data_in.model_dump(),
        **{"serviceClassValueId": str(uuid.uuid4())},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/serviceClassValue/{serviceClassValueId}",
    description=DESC_UPDATE,
)
def update_service_class_value(
    data_in: schemas.ServiceClassValueUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    service_class_value_id: str = Path(
        ..., title="serviceClassValue ID", alias="serviceClassValueId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update service class value request from {username} with partner "
        f"id {partner_id} and service class value id {service_class_value_id}"
    )

    data_out = schemas.ServiceClassValueInDb(
        **data_in.model_dump(),
        **{"serviceClassValueId": service_class_value_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/serviceClassValue/{serviceClassValueId}",
    description=DESC_DELETE,
)
def delete_service_class_value(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    service_class_value_id: str = Path(
        ..., title="serviceClassValue ID", alias="serviceClassValueId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete service class value request from {username} with partner "
        f"id {partner_id} and service class value id {service_class_value_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Service class Qos API
@router.post(
    "/v1/partners/{partnerId}/network/serviceClassQos", description=DESC_CREATE
)
def create_service_class_qos(
    data_in: schemas.ServiceClassQosCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create service class qos request from {username} with partner "
        f"id {partner_id}"
    )

    data_out = schemas.ServiceClassQosInDb(
        **data_in.model_dump(),
        **{"serviceClassQosId": str(uuid.uuid4())},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/serviceClassQos/{serviceClassQosId}",
    description=DESC_UPDATE,
)
def update_service_class_qos(
    data_in: schemas.ServiceClassQosUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    service_class_qos_id: str = Path(
        ..., title="serviceClassQos ID", alias="serviceClassQosId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update service class qos request from {username} with partner "
        f"id {partner_id} and service class qos id {service_class_qos_id}"
    )

    data_out = schemas.ServiceClassQosInDb(
        **data_in.model_dump(),
        **{"serviceClassQosId": service_class_qos_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/serviceClassQos/{serviceClassQosId}",
    description=DESC_DELETE,
)
def delete_service_class_qos(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    service_class_qos_id: str = Path(
        ..., title="serviceClassQos ID", alias="serviceClassQosId"
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete service class qos request from {username} with partner "
        f"id {partner_id} and service class qos id {service_class_qos_id}"
    )

    return status.HTTP_204_NO_CONTENT


# SCN profile API
@router.post("/v1/partners/{partnerId}/network/scnProfile", description=DESC_CREATE)
def create_scn_profile(
    data_in: schemas.ScnProfileCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create scn profile request from {username} with partner "
        f"id {partner_id}"
    )

    data_out = schemas.ScnProfileInDb(
        **data_in.model_dump(),
        **{"scnProfileId": str(uuid.uuid4())},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/scnProfile/{scnProfileId}",
    description=DESC_UPDATE,
)
def update_scn_profile(
    data_in: schemas.ScnProfileUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    scn_profile_id: str = Path(..., title="scnProfile ID", alias="scnProfileId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update scn profile request from {username} with partner "
        f"id {partner_id} and scn profile id {scn_profile_id}"
    )

    data_out = schemas.ScnProfileInDb(
        **data_in.model_dump(),
        **{"scnProfileId": scn_profile_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/scnProfile/{scnProfileId}",
    description=DESC_DELETE,
)
def delete_scn_profile(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    scn_profile_id: str = Path(..., title="scnProfile ID", alias="scnProfileId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete scn profile request from {username} with partner "
        f"id {partner_id} and scn profile id {scn_profile_id}"
    )

    return status.HTTP_204_NO_CONTENT
