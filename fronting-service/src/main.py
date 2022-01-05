# flask_example.py
import flask
import requests

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

print("init")

span_exporter = OTLPSpanExporter(
    endpoint="http://otel-collector:4317",
    insecure=True
)
tracer_provider = TracerProvider(resource=Resource.create({SERVICE_NAME: "fronting-service"}))
trace.set_tracer_provider(tracer_provider)
span_processor = BatchSpanProcessor(span_exporter)
tracer_provider.add_span_processor(span_processor)

app = flask.Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

tracer = trace.get_tracer(__name__)


@app.route("/")
def index():
    response = requests.get("http://backend-service:4567/slow-endpoint")
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)
