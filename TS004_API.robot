# -----------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------
*** Settings ***
# ------------------------------------------------------------------
Documentation   This file is used to test the Rampnet web app Reports page.

Library     RequestsLibrary
Library  JSONLibrary
Library  os
Library  Collections
# ------------------------------------------------------------------
*** Variables ***
# ------------------------------------------------------------------
# Test suite global variables (ALL_CAPS)
${base_url}         http://inp00554:8080/secureeye-server/rest-avatar/v1
${base_url_geo}     http://inp00554:8080/secureeye-server/rest/v1
${base_url_reports}     http://inp00554:8080/secureeye-server/rest-avatar/v1/reports
${base_url_tracks}     http://inp00554:8080/secureeye-server/rest/v1/tracks
${api_getAllVehicles}    vehicles
${api_getAllVehiclesTypes}    vehicles/vehicletypes
${api_getSensors_byId}    sensors
${api_getGse}       gse
${api_getGeofence}  zones
${tracks}       latesttracks
${api_getAllSearchPoints}   searchpoint
${date_time}    2019-04-09T11:20/2019-04-09T11:25
${Access_Token}  Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlX25hbWUiOm51bGwsInBhc3N3b3JkIjoiJDJhJDExJHgyaEVYUERGc0kueVZyV1ZVWU93RC5MXC83VjlXYlZqcFhCMEk3RmRUTm8zbTJFOFM4Y3Z5dSIsImFkbWluX2NvbnNvbGVfYWNjZXNzIjpudWxsLCJyb2xlIjpudWxsLCJ1c2VyX2lkIjoiYXZhdGFyIiwiaGFzX3RpbWVvdXQiOm51bGwsIm1vYmlsZV9ubyI6IjExMTExMTExMTEiLCJlbWFpbGlkIjoiYXZhdGFyQHJvY2t3ZWxsY29sbGlucy5jb20iLCJpZCI6MSwidXNlciI6IkEgQXZhdGFyIiwiaWF0IjoxNTM0OTIzNjMwNzEwLCJ0aW1lb3V0IjpudWxsfQ.yCqRjzgmvELhlx_T88ZVr99aMReUb2s4HxoGfo512yc

# ------------------------------------------------------------------
*** Keywords ***
# ------------------------------------------------------------------

# ------------------------------------------------------------------
*** Test Cases ***
# ------------------------------------------------------------------

TC001_API_getAllVehicles
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Vehicles
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getAllVehicles}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200
    ${json_obj}=    to json  ${response.content}
    #log to console  ${json_obj}
    ${veh_number}=    get value from json  ${json_obj}  $.entity.vehicles[:1].contract_type
    ${new}=     convert to string   ${veh_number}
    log to console  ${new}
    should be equal   ${new}  'Permanent'


TC002_API_getAllVehiclesTypes
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Vehicles
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession  ${api_getAllVehiclesTypes}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC003_API_getVehiclesById
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Vehicles
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getAllVehicles}/13   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC004_API_getAllVehicles_ById
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Vehicles
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getAllVehicles}/13   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC005_API_getSensors_byId
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Vehicles
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getSensors_byId}/1   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC006_API_getSensors
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Sensors
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getSensors_byId}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC007_API_getGse
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Gse
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getGse}/types/13   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC008_API_getAllGse
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Gse
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getGse}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC009_API_getAllGseOperator
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Gse
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getGse}/operatorinfo   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC010_API_GetGeoFenceById
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Geofence
    create session   mysession      ${base_url_geo}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getGeofence}/51   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC011_API_getAllGeoFences
    [Documentation]  Verify that the Asset violations download in the Different format
    [Tags]  web_api  Geofence
    create session   mysession      ${base_url_geo}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getGeofence}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC012_API_getAllSearchPoints
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getAllSearchPoints}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC013_API_getReports
    create session   mysession      ${base_url_reports}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${api_getAllVehicles}   ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC014_API_getAlerts
    create session   mysession      ${base_url_reports}/alerts
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC015_API_getTotalViolationCount
    create session   mysession      ${base_url_reports}/violationTypeChart
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC016_API_GetGseOperatorWiseViolationCount
    create session   mysession      ${base_url_reports}/operatorWiseViolationCount
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC017_API_GetVehicleBodyTypeWiseViolationCount
    create session   mysession      ${base_url_reports}/vehicleBodyTypeWiseViolationCount
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC018_API_vehicleBodyTypeWiseViolationFilterByOperator
    create session   mysession      ${base_url_reports}/vehicleBodyTypeWiseViolationFilterByOperator/BWFS
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC019_API_vehicleWiseViolationFilterByBodyType
    create session   mysession      ${base_url_reports}/vehicleWiseViolationFilterByBodyType/LMV
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC020_API_vehicleWiseViolationFilterByBodyType
    create session   mysession      ${base_url_reports}/vehicleWiseViolationFilterByBodyType/LMV
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC021_API_GetvehicleViolationListFilterByBodyTypeAndOperator
    create session   mysession      ${base_url_reports}/vehicleViolationListFilterByBodyTypeAndOperator
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC022_API_assetTypeViolationCount
    create session   mysession      ${base_url_reports}/assetTypeViolationCount
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC023_API_GetdetailedVehicleViolationCount
    create session   mysession      ${base_url_reports}/detailedVehicleViolationCount
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC024_API_GetalertsFormatted
    create session   mysession      ${base_url_reports}/alertsFormatted
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC025_API_GetGseFormattedData
    create session   mysession      ${base_url_reports}/historyFormatted
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200


TC026_API_GetSpeedAlertFormatted
    create session   mysession      ${base_url_reports}/speedalertsFormatted
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC027_API_getAdsb-Data
    create session   mysession      ${base_url_tracks}/history
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC028_API_LastKnowPosition
    create session   mysession      ${base_url_tracks}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   ${tracks}/GSEs  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC029_API_LastKnowPositionTimeInterval
    create session   mysession      ${base_url_tracks}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /latesttracksTimeWindow/GSEs/5  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC030_API_getAllVehicleBodyTypes
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC031_API_getAllVehicleBodyTypesByAirlines
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type/airlines  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC032_API_getAllVehicleBodyTypesById
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type/2  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC033_API_getAllVehicleBodyTypes_types
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type/types  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC034_API_getAllVehicleBodyTypesByOperators
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type/operators  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC035_API_getAllVehicleBodyTypesByTrackId
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type/trackid  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC036_API_getAllVehicleBodyTypesByAssetTypes
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /vehicle_body_type/assettypes  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC037_API_getGateway
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /gateway  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC038_API_getGateWayByID/IP
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /gateway/byIpOrId?id=1  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC039_API_getReportIncidentByID
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /incident/1  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC040_API_getReportIncidents
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   /incident/${date_time}  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200

TC041_API_getVehicleImage_BySensorID
    create session   mysession      ${base_url}
    ${Auth}=     create dictionary   Authorization=${Access_Token}
    ${response}=     get request     mysession   vehicles/image/00-04-a3-0b-00-22-05-6e  ${Auth}
    log to console  ${response.status_code}
    ${status_code}=     convert to string  ${response.status_code}
    should be equal  ${status_code}    200
