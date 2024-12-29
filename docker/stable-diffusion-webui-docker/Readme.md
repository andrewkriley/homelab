- Need to add instructions for https://github.com/AbdBarho/stable-diffusion-webui-docker/wiki/Usage
- - inc istype issue in Docker File and adding --api to the start. 

 added by ANDRERIL to remove Type error during install in DOCKERFILE<br>
RUN --mount=type=cache,target=/root/.cache/pip \
   pip uninstall -y typing_extensions && \
   pip install typing_extensions==4.11.0
<p>
added --api by ANDRERIL in DOCKERFILE <br>
CMD python -u webui.py --listen --api --port 7860 ${CLI_ARGS}
