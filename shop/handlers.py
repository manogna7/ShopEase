from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def handle_product_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Product created: {instance.name}")

def custom_exception_handler(exc, context):
    response = exception_handler(exc. context)

    if response is not None:
        custom_response_data = {
            'errors': response.data,
            'status_code': response.status_code
        }
        response.data = custom_response_data

    return response