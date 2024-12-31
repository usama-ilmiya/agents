from fastapi import APIRouter, UploadFile, File, HTTPException
from pra.utils.audio_utils import process_audio_files
from pra.utils.text_utils import recognize_speech_whisper
from pathlib import Path
import tempfile
import shutil

router = APIRouter()


@router.post("/compare-audio")
async def compare_audio(
    reference_file: UploadFile = File(...),
    recorded_file: UploadFile = File(...),
    target_word: str = "الرحمن",
):
    """
    Compare a reference audio file with a recorded file using DTW and Whisper.
    """
    try:
        # Temporary directory for saving files
        with tempfile.TemporaryDirectory() as temp_dir:
            ref_path = Path(temp_dir) / reference_file.filename
            rec_path = Path(temp_dir) / recorded_file.filename
            print(ref_path)
            print(rec_path)
            with ref_path.open("wb") as ref_out:
                shutil.copyfileobj(reference_file.file, ref_out)

            with rec_path.open("wb") as rec_out:
                shutil.copyfileobj(recorded_file.file, rec_out)

            # Recognize speech using Whisper
            found, target = recognize_speech_whisper(str(rec_path), target_word)
            # if not is_word_match:
            #     return {
            #         "match": False,
            #         "message": "Spoken word does not match the target word.",
            #     }

            # Calculate pronunciation similarity
            result = process_audio_files(str(ref_path), str(rec_path))
            return {
                "recognized": found,
                "target": target,
                "match": found == target,
                "dtw_distance": result["dtw_distance"],
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")
