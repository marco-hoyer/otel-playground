require 'opentelemetry/sdk'
require 'opentelemetry/exporter/otlp'
require 'rubygems'
require 'bundler/setup'
Bundler.require

set :bind, '0.0.0.0'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'backend-service'
  c.service_version = '1.2.3'
  c.use_all
end

get '/' do
  'Hello world!'
end

get '/slow-endpoint' do
  sleep(2)
  'I am pretty slow but done now after 2s'
end
