import uuid

import grpc

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from CRM.address_pb2_grpc import NRIStub
from CRM.address_pb2 import ServiceRequest

app = FastAPI()

data = {}


class Address(BaseModel):
    street: str
    house: str


class UserRequest(BaseModel):
    id: Optional[str]
    name: str
    surname: str
    phone_number: str
    address: Address


class NRIResponse(BaseModel):
    equipment_url: str


@app.get("/{request_id}")
def get_user_request(request_id):
    return data.get(request_id)


@app.post("/user_requests/")
def create_user_request(user_request: UserRequest):
    request_id = uuid.uuid4().hex
    user_request.id = request_id
    data[request_id] = user_request

    print("Starting gRPC connection...")
    channel = grpc.insecure_channel("nri:8080")
    client = NRIStub(channel)
    print("gRPC connection established!")

    print("Sending request...")
    request = ServiceRequest(
        street=user_request.address.street,
        house=user_request.address.house,
    )

    rpc_response = client.Check(request)
    response = NRIResponse(equipment_url=rpc_response.equipment_url)

    return response
