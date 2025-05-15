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
router = APIRouter(tags=["ISP APIs"])


# Buhm APIs
@router.post(
    "/v1/partners/{partnerId}/network/buhm",
    description=DESC_CREATE,
)
def create_buhm(
    data_in: schemas.BuhmCreate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create buhm request from {username} with partner "
        f"id {partner_id}"
    )

    data_out = schemas.BuhmInDb(
        **data_in.model_dump(), **{"buhmId": "554aab05-dd7f-44ec-be0c-749eb083505c"}
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put("/v1/partners/{partnerId}/network/buhm/{buhmId}", description=DESC_UPDATE)
def update_buhm(
    data_in: schemas.BuhmUpdate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    buhm_id: str = Path(..., title="Buhm ID", alias="buhmId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update buhm request from {username} with partner id "
        f"{partner_id} and buhm id {buhm_id}"
    )

    data_out = schemas.BuhmInDb(**data_in.model_dump(), **{"buhmId": buhm_id})

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/buhm/{buhmId}",
    description=DESC_DELETE,
)
def delete_buhm(
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    buhm_id: str = Path(..., title="Buhm ID", alias="buhmId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete buhm request from {username} with partner id "
        f"{partner_id} and buhm id {buhm_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Hub APIs


@router.post("/v1/partners/{partnerId}/network/hub", description=DESC_CREATE)
def create_hub(
    data_in: schemas.HubCreate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create hub request from {username} with "
        f"partner id {partner_id}"
    )

    data_out = schemas.HubInDb(
        **data_in.model_dump(),
        **{
            "hubId": "554aab05-dd7f-44ec-be0c-749eb083505c",
            "parentHubName": data_in.refParentHubName,
        },
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put("/v1/partners/{partnerId}/network/hub/{hubId}", description=DESC_UPDATE)
def update_hub(
    data_in: schemas.HubUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    hub_id: str = Path(..., title="Hub ID", alias="hubId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update hub request from {username} with partner id "
        f"{partner_id} and hub id {hub_id}"
    )

    data_out = schemas.HubInDb(
        **data_in.model_dump(),
        **{
            "hubId": hub_id,
            "parentHubName": data_in.refParentHubName,
        },
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete("/v1/partners/{partnerId}/network/hub/{hubId}", description=DESC_DELETE)
def delete_hub(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    hub_id: str = Path(..., title="Hub ID", alias="hubId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete hub request from {username} with partner id "
        f"{partner_id} and hub id {hub_id}"
    )

    return status.HTTP_204_NO_CONTENT


# Site intent APIs
@router.post("/v1/partners/{partnerId}/network/siteIntent", description=DESC_CREATE)
def create_site_intent(
    data_in: schemas.SiteIntentCreate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create site intent request from {username} with "
        f"partner id {partner_id}"
    )

    data_out = schemas.SiteIntentInDb(
        **data_in.model_dump(),
        **{"siteIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/siteIntent/{siteIntentId}",
    description=DESC_UPDATE,
)
def update_site_intent(
    data_in: schemas.SiteIntentUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    site_intent_id: str = Path(..., title="siteIntent ID", alias="siteIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update site intent request from {username} with partner id "
        f"{partner_id} and site intent id {site_intent_id}"
    )

    data_out = schemas.SiteIntentInDb(
        **data_in.model_dump(), **{"siteIntentId": site_intent_id}
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/siteIntent/{siteIntentId}",
    description=DESC_DELETE,
)
def delete_site_intent(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    site_intent_id: str = Path(..., title="siteIntent ID", alias="siteIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete site intent request from {username} with partner id "
        f"{partner_id} and site intent id {site_intent_id}"
    )

    return status.HTTP_204_NO_CONTENT


# CPOD intent APIs


@router.post("/v1/partners/{partnerId}/network/cpodIntent", description=DESC_CREATE)
def create_cpod_intent(
    data_in: schemas.CpodIntentCreate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create cpod intent request from {username} with "
        f"partner id {partner_id}"
    )

    data_out = schemas.CpodIntentInDb(
        **data_in.model_dump(),
        **{"cpodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/cpodIntent/{cpodIntentId}",
    description=DESC_UPDATE,
)
def update_cpod_intent(
    data_in: schemas.CpodIntentUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    cpod_intent_id: str = Path(..., title="cpodIntent ID", alias="cpodIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update cpod intent request from {username} with partner id "
        f"{partner_id} and cpod intent id {cpod_intent_id}"
    )

    data_out = schemas.CpodIntentInDb(
        **data_in.model_dump(),
        **{"cpodIntentId": cpod_intent_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/cpodIntent/{cpodIntentId}",
    description=DESC_DELETE,
)
def delete_cpod_intent(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    cpod_intent_id: str = Path(..., title="cpodIntent ID", alias="cpodIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete cpod intent request from {username} with partner id "
        f"{partner_id} and cpod intent id {cpod_intent_id}"
    )

    return status.HTTP_204_NO_CONTENT


# PPOD intent APIs
@router.post("/v1/partners/{partnerId}/network/ppodIntent", description=DESC_CREATE)
def create_ppod_intent(
    data_in: schemas.PpodIntentCreate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create ppod intent request from {username} with "
        f"partner id {partner_id}"
    )

    data_out = schemas.PpodIntentInDb(
        **data_in.model_dump(),
        **{
            "cpodIntentId": data_in.refCpodIntentId,
            "ppodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
        },
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/ppodIntent/{ppodIntentId}",
    description=DESC_UPDATE,
)
def update_ppod_intent(
    data_in: schemas.PpodIntentUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    ppod_intent_id: str = Path(..., title="ppodIntent ID", alias="ppodIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update ppod intent request from {username} with partner id "
        f"{partner_id} and ppod intent id {ppod_intent_id}"
    )

    data_out = schemas.PpodIntentInDb(
        **data_in.model_dump(),
        **{
            "cpodIntentId": data_in.refCpodIntentId,
            "ppodIntentId": ppod_intent_id,
        },
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/ppodIntent/{ppodIntentId}",
    description=DESC_DELETE,
)
def delete_ppod_intent(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    ppod_intent_id: str = Path(..., title="ppodIntent ID", alias="ppodIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete ppod intent request from {username} with partner id "
        f"{partner_id} and ppod intent id {ppod_intent_id}"
    )

    return status.HTTP_204_NO_CONTENT


# DAAS intent APIs


@router.post("/v1/partners/{partnerId}/network/daasIntent", description=DESC_CREATE)
def create_daas_intent(
    data_in: schemas.DaasIntentCreate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create daas intent request from {username} with "
        f"partner id {partner_id}"
    )

    data_out = schemas.DaasIntentInDb(
        **data_in.model_dump(),
        **{"daasIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/daasIntent/{daasIntentId}",
    description=DESC_UPDATE,
)
def update_daas_intent(
    data_in: schemas.DaasIntentUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    daas_intent_id: str = Path(..., title="daasIntent ID", alias="daasIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update daas intent request from {username} with partner id "
        f"{partner_id} and daas intent id {daas_intent_id}"
    )

    data_out = schemas.DaasIntentInDb(
        **data_in.model_dump(), **{"daasIntentId": daas_intent_id}
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/daasIntent/{daasIntentId}",
    description=DESC_DELETE,
)
def delete_daas_intent(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    daas_intent_id: str = Path(..., title="daasIntent ID", alias="daasIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete daas intent request from {username} with partner id "
        f"{partner_id} and daas intent id {daas_intent_id}"
    )

    return status.HTTP_204_NO_CONTENT


# HAGG intent APIs
@router.post("/v1/partners/{partnerId}/network/haggIntent", description=DESC_CREATE)
def create_hagg_intent(
    data_in: schemas.HaggIntentCreate,
    partner_id: str = Path(
        ...,
        title="Partner ID",
        alias="partnerId",
    ),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a create hagg intent request from {username} with "
        f"partner id {partner_id}"
    )

    data_out = schemas.HaggIntentinDb(
        **data_in.model_dump(),
        **{"haggIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c"},
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(data_out),
    )


@router.put(
    "/v1/partners/{partnerId}/network/haggIntent/{haggIntentId}",
    description=DESC_UPDATE,
)
def update_hagg_intent(
    data_in: schemas.HaggIntentUpdate,
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    hagg_intent_id: str = Path(..., title="haggIntent ID", alias="haggIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> JSONResponse:
    log.info(
        f"Received a update hagg intent request from {username} with partner id "
        f"{partner_id} and hagg intent id {hagg_intent_id}"
    )

    data_out = schemas.HaggIntentinDb(
        **data_in.model_dump(),
        **{"haggIntentId": hagg_intent_id},
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(data_out),
    )


@router.delete(
    "/v1/partners/{partnerId}/network/haggIntent/{haggIntentId}",
    description=DESC_DELETE,
)
def delete_hagg_intent(
    partner_id: str = Path(..., title="Partner ID", alias="partnerId"),
    hagg_intent_id: str = Path(..., title="haggIntent ID", alias="haggIntentId"),
    username: str = Depends(security.Security()),
    client_id: Optional[str] = Query(None, alias="clientId"),
) -> int:
    log.info(
        f"Received a delete hagg intent request from {username} with partner id "
        f"{partner_id} and hagg intent id {hagg_intent_id}"
    )

    return status.HTTP_204_NO_CONTENT
