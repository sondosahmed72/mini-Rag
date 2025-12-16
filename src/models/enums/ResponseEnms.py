from enum import Enum
class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_support"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS ="file_uploaded_success"
    FILE_UPLOAD_FAILED ="file_uploaded_failed"
    FILE_VALIDATED_SUCCESS = "file_validate_successfully"