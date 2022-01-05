FROM ruby:2.7.2

COPY . /app

WORKDIR /app
RUN bundle install

CMD ["ruby", "/app/server.rb"]
