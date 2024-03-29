import json
import os

import requests


def create_session(github_token):
    sess = requests.Session()
    sess.headers = {
        "Accept": "; ".join([
            "application/vnd.github.v3+json"
        ]),
        "Authorization": f"token {github_token}",
        "User-Agent": f"GitHub Actions script in {__file__}"
    }

    def raise_for_status(resp, *args, **kwargs):
        try:
            resp.raise_for_status()
        except Exception:
            print(resp.text)
            sys.exit("Error: Invalid repo, token or network issue!")

    sess.hooks["response"].append(raise_for_status)
    return sess


if __name__ == "__main__":
    event_path = os.environ["GITHUB_EVENT_PATH"]
    github_token = os.environ["GITHUB_TOKEN"]
    sess = create_session(github_token)
    event_data = json.load(open(event_path))
    print(f"--- event_data: {event_data}")
    #
    # check_suite = event_data["check_suite"]
    # status = check_suite["status"]
    #
    # if status != "completed":
    #     print(f"*** Check run has not completed")
    #     sys.exit(78)
    #
    # assert len(check_suite["pull_requests"]) == 1
    # pull_request = check_suite["pull_requests"][0]
    # pr_number = pull_request["number"]
    # pr_src = pull_request["head"]["ref"]
    # pr_dst = pull_request["base"]["ref"]
    #
    # print(f"*** Checking pull request #{pr_number}: {pr_src} ~> {pr_dst}")
    #
    # pr_data = sess.get(pull_request["url"]).json()
    #
    # pr_title = pr_data["title"]
    # print(f"*** Title of PR is {pr_title!r}")
    # if pr_title.startswith("[WIP] "):
    #     print("*** This is a WIP PR, will not merge")
    #     sys.exit(78)
    #
    # pr_user = pr_data["user"]["login"]
    # print(f"*** This pull request was opened by {pr_user}")
    # sys.exit(78)
    #
    # print("*** This pull request is ready to be merged.")
    # merge_url = pull_request["url"] + "/merge"
    # sess.put(merge_url)
    #
    # print("*** Cleaning up pull request branch")
    # pr_ref = pr_data["head"]["ref"]
    # api_base_url = pr_data["base"]["repo"]["url"]
    # ref_url = f"{api_base_url}/git/refs/heads/{pr_ref}"
    # sess.delete(ref_url)
