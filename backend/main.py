import json
import logging

from flask import Flask, jsonify, request
from promptflow import load_flow
from promptflow.connections import AzureOpenAIConnection
from promptflow.entities import FlowContext
from promptflow.exceptions import SystemErrorException, UserErrorException


class LawGptBackend(Flask):
    pass


app = LawGptBackend(__name__)
logging.basicConfig(format="%(threadName)s:%(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# load flow as a function, the function object can be shared accross threads.
f = load_flow("./pf/")


@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, UserErrorException):
        return jsonify({"message": e.message, "additional_info": e.additional_info}), 400
    elif isinstance(e, SystemErrorException):
        return jsonify({"message": e.message, "additional_info": e.additional_info}), 500
    else:
        from promptflow._internal import ErrorResponse, ExceptionPresenter

        # handle other unexpected errors, can use internal class to format them
        # but interface may change in the future
        presenter = ExceptionPresenter.create(e)
        trace_back = presenter.formatted_traceback

        resp = ErrorResponse(presenter.to_dict(include_debug_info=False))
        response_code = resp.response_code
        result = resp.to_simplified_dict()
        result.update({"trace_back": trace_back})
        return jsonify(result), response_code


@app.route("/health", methods=["GET"])
def health():
    """Check if the runtime is alive."""
    return {"status": "ok"}


@app.route("/analyseCase", methods=["POST"])
def analyseCase():
    """process a flow request in the runtime."""
    raw_data = request.get_data()
    logger.info(f"Start loading request data '{raw_data}'.")
    data = json.loads(raw_data)
    logger.info(f"Start loading request data '{data}'.")

#     data = dict({'text': """


#
# """, 'reference': ''})

    # configure flow contexts, create a new context object for each request to make sure they are thread safe.
    f.context = FlowContext()
    result_dict = f(**data)
    print(result_dict)
    # Note: if specified streaming=True in the flow context, the result will be a generator
    # reference promptflow._sdk._serving.response_creator.ResponseCreator on how to handle it in app.
    # return jsonify(result_dict)
    return {"status": "ok", "result": result_dict["output_prompt"]}


def create_app(**kwargs):
    return app


if __name__ == "__main__":
    # test this with curl -X POST http://0.0.0.0:5000/score --header "Content-Type: application/json" --data '{"flow_input": "some_flow_input", "node_input": "some_node_input"}'  # noqa: E501
    create_app().run(debug=True, host='0.0.0.0', port=5001)
