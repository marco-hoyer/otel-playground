# Open Telemetry Playground

## Why? 

The idea is to have a standardised set of apps working together to simulate tracing with different providers.
With an Open Telemetry agent in place collecting all the information it's easy to send telemetry to different and multiple providers.

## How to use it

### Preparation

* check the `aws-otel-collector/otel-local-config.yaml` file and set API Keys for PagerDuty, HoneyComb and DataDog

### Startup

    docker-compose up --build

### Send request

This sends a request to the api-proxy which will be delayed in a slow backend service for 2 seconds.

    curl localhost:6666

## Intetrated providers

* https://app.lightstep.com/solarisbank-ag-dev-6af6c780
* https://one.eu.newrelic.com
* https://app.datadoghq.eu
* https://ui.honeycomb.io/sre-17/
* https://solarisbank.grafana.net/