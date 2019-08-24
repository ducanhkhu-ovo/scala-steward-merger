FROM python:3-alpine

LABEL "com.github.actions.name"="Auto-merge my pull requests"
LABEL "com.github.actions.description"="Merge and clean-up the pull request after the checks pass"
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="green"

COPY requirements.txt /requirements.txt
RUN	pip3 install -r /requirements.txt

COPY merger.py /merger.py

ENTRYPOINT [ "sh", "-c", "echo $GITHUB_TOKEN" ]
