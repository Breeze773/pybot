FROM public.ecr.aws/lambda/python:3.8

# Copy function code
RUN pip install json
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
