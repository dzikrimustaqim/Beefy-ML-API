FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r /code/requirements.txt

RUN pip install python-multipart

COPY . /code

RUN wget --no-check-certificate 'https://download1980.mediafire.com/ob5057pwitpgMK9TOKsAQBJ0xNRIu5f2vCiNjyPtQjcrM0jcP1gRcGVTCTiDUeQWu1ov55f3eZFPB6bhdsIXoS4WlNNWSGUQRd8jnTrSy82bM9eu16nhpy_rposaaGHxiP62ZbDCOyHvW6xvuPw15BdHbmmh0SUvxciiXrqJ-UmvyhgV/fl67w6t0qx3mk1i/softmax_new_model.h5' -O '/code/models/softmax_new_model.h5'

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "8080"]
