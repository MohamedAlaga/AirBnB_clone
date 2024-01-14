#!/bin/usr/python3
"""This module defines a class city that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class that inherits from BaseModel"""
    state_id = ""
    name = ""
