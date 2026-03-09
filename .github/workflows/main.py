name: Build APK
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-20.04
    steps:
      - uses: actions/checkout@v3

      - name: Build with Buildozer
        uses: ArtemSerebriakov/buildozer-action@v1
        with:
          buildozer_version: master
          command: buildozer android debug
          repository_root: .
