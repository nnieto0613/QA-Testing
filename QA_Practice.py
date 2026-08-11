import pytest

# 1. The MainFeature 
def validate_audio_file(file_name):
    """
    Validates that the uploaded file is an allowed audio format 
    before initiating the librosa and pandas detection models.
    """
    allowed_extensions = ['.wav', '.mp3']
    if not any(file_name.endswith(ext) for ext in allowed_extensions):
        raise ValueError("Invalid File Type: Only .wav and .mp3 are supported.")
    return True

# 2. Automation Tests 
def test_valid_mp3_upload():
    # Test that a valid mp3 file passes validation
    result = validate_audio_file("track_01.mp3")
    assert result == True

def test_valid_wav_upload():
    # Test that a valid wav file passes validation
    result = validate_audio_file("sample_beat.wav")
    assert result == True

def test_invalid_pdf_upload_returns_error():
    # Test the exact edge case from the bug report: uploading a PDF
    with pytest.raises(ValueError) as error_info:
        validate_audio_file("document.pdf")
    
    # Verify the system returns a safe error message instead of a raw traceback
    assert "Invalid File Type" in str(error_info.value)