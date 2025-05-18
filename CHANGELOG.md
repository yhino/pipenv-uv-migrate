# CHANGELOG


## v0.2.3 (2025-05-18)

### :arrow_up:

- :arrow_up: Bump astral-sh/setup-uv from 5 to 6
  ([#15](https://github.com/yhino/pipenv-uv-migrate/pull/15),
  [`80cfa4c`](https://github.com/yhino/pipenv-uv-migrate/commit/80cfa4c1c2d4dc82fa180e989423e55161b50ced))

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#13](https://github.com/yhino/pipenv-uv-migrate/pull/13),
  [`533324a`](https://github.com/yhino/pipenv-uv-migrate/commit/533324a0d5aa82336e8bde385623380b2c18f91c))

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#17](https://github.com/yhino/pipenv-uv-migrate/pull/17),
  [`c0ff50c`](https://github.com/yhino/pipenv-uv-migrate/commit/c0ff50c505c9772305f2eb16ddfb8725b0f31e9c))

### :bug:

- :bug: compatible with removal of CliRunner mix_stderr parameter in Click 8.2.0
  ([#18](https://github.com/yhino/pipenv-uv-migrate/pull/18),
  [`9f284da`](https://github.com/yhino/pipenv-uv-migrate/commit/9f284da3a0e1ea20518ffdd08519e510897816e7))

* :bug: compatible with removal of CliRunner mix_stderr parameter in Click 8.2.0

see https://github.com/pallets/click/releases/tag/8.2.0

* :bug: run on old interface with python 3.9 only

- :bug: fix misconfigured build-backend ([#19](https://github.com/yhino/pipenv-uv-migrate/pull/19),
  [`69a2871`](https://github.com/yhino/pipenv-uv-migrate/commit/69a287134de9c28894b1c910de0989018fa719d7))

- :bug: fix warning, run uv in tox ([#16](https://github.com/yhino/pipenv-uv-migrate/pull/16),
  [`19dc5d4`](https://github.com/yhino/pipenv-uv-migrate/commit/19dc5d4ce3638352dd703dca3a1d4c53c44556c7))

fix "warning: `VIRTUAL_ENV=.tox/py` does not match the project environment path `.venv` and will be
  ignored"

### Other

- :bookmark: v0.2.3
  ([`847eb31`](https://github.com/yhino/pipenv-uv-migrate/commit/847eb31e724acd61e7fd32e08f148126aade4b52))

- Fix migration when multiple source exist, including pypi
  ([#21](https://github.com/yhino/pipenv-uv-migrate/pull/21),
  [`7c245ed`](https://github.com/yhino/pipenv-uv-migrate/commit/7c245ed62bf90f9def4fc8058484476e2fce471f))

* :test_tube: update testdata

* :bug: fix migration when multiple source exist, including pypi

ref. https://docs.astral.sh/uv/configuration/indexes/#pinning-a-package-to-an-index

* :white_check_mark: add migration test when single source exists

* :bug: fix to not output empty sections

- Fix test action ([#14](https://github.com/yhino/pipenv-uv-migrate/pull/14),
  [`770124e`](https://github.com/yhino/pipenv-uv-migrate/commit/770124e3b64cf776e20893e2ec40fed2eb6fc1f9))

* :construction_worker: run test on a schedule

* :bug: fix warning from codecov


## v0.2.2 (2025-03-02)

### :arrow_up:

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#11](https://github.com/yhino/pipenv-uv-migrate/pull/11),
  [`080d8dd`](https://github.com/yhino/pipenv-uv-migrate/commit/080d8ddd3d1549815f27097d52d2785a0922c4fc))

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#12](https://github.com/yhino/pipenv-uv-migrate/pull/12),
  [`7af7e5c`](https://github.com/yhino/pipenv-uv-migrate/commit/7af7e5c2855a18f1af6186f598fe59d2bc41517b))

### Other

- :bookmark: v0.2.2
  ([`454bb54`](https://github.com/yhino/pipenv-uv-migrate/commit/454bb54f631f8b4338f5b686305135c02897305f))


## v0.2.1 (2025-02-02)

### :arrow_up:

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#10](https://github.com/yhino/pipenv-uv-migrate/pull/10),
  [`b496443`](https://github.com/yhino/pipenv-uv-migrate/commit/b496443d69654d028198fceab96869636c571cfb))

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#9](https://github.com/yhino/pipenv-uv-migrate/pull/9),
  [`c3f590d`](https://github.com/yhino/pipenv-uv-migrate/commit/c3f590da8157cc2641b800e0905cfe8fd7fa1a4e))

### Other

- :bookmark: v0.2.1
  ([`8258a5d`](https://github.com/yhino/pipenv-uv-migrate/commit/8258a5db7ae751bc875321f993b021f7c1b61cb1))


## v0.2.0 (2025-01-01)

### :arrow_up:

- :arrow_up: Bump astral-sh/setup-uv from 4 to 5
  ([#5](https://github.com/yhino/pipenv-uv-migrate/pull/5),
  [`7402080`](https://github.com/yhino/pipenv-uv-migrate/commit/74020805b050c5cd9561799ade03d4e87c909e79))

- :arrow_up: Bump python-semantic-release/python-semantic-release
  ([#1](https://github.com/yhino/pipenv-uv-migrate/pull/1),
  [`66288ea`](https://github.com/yhino/pipenv-uv-migrate/commit/66288eab8fd3f72fcd27f7145236d32cd24d8420))

### :sparkles:

- :sparkles: Python 3.8 EOL
  ([`7a12e7e`](https://github.com/yhino/pipenv-uv-migrate/commit/7a12e7e84e5d27d20a8bc8b395f5c525b7147ed9))

### Other

- :bookmark: v0.2.0
  ([`a20385f`](https://github.com/yhino/pipenv-uv-migrate/commit/a20385fefc6df15ad99aa97aac4b0218e5616394))

- :fire: remove uv.lock ([#7](https://github.com/yhino/pipenv-uv-migrate/pull/7),
  [`5a91957`](https://github.com/yhino/pipenv-uv-migrate/commit/5a91957bae67b7a060c3d5b13da01e1abf493a12))

- :pencil: add classifiers to dist package ([#8](https://github.com/yhino/pipenv-uv-migrate/pull/8),
  [`b2e0c65`](https://github.com/yhino/pipenv-uv-migrate/commit/b2e0c65458dc89c021c04c555b36050abdba4cc7))

- Merge pull request #3 from cclauss/patch-1
  ([`43b573f`](https://github.com/yhino/pipenv-uv-migrate/commit/43b573f8ff72cdfb6be5100b3aaa8708fc109482))

- Merge pull request #4 from cclauss/patch-2
  ([`babaa1f`](https://github.com/yhino/pipenv-uv-migrate/commit/babaa1fc9c951c1aff051a4821314aa751d9cf5f))

test.yml: Add Python 3.13 to the testing

- Merge pull request #6 from yhino/eol-python38
  ([`24d3e47`](https://github.com/yhino/pipenv-uv-migrate/commit/24d3e4755ffe0e1c84d7605838c3bc67aba319a2))

:sparkles: Python 3.8 EOL

- Readme.md: `uv tool install pipenv-uv-migrate`
  ([`0d121d2`](https://github.com/yhino/pipenv-uv-migrate/commit/0d121d24b8c9f42687f63efb884f899af7dfb54a))

- Test.yml: Add Python 3.13 to the testing
  ([`45b5eb7`](https://github.com/yhino/pipenv-uv-migrate/commit/45b5eb7f2b2202d5ba7f66f37b5f0a310634f400))

- Uvx tox@latest --with tox-uv -e py
  ([`77e06ec`](https://github.com/yhino/pipenv-uv-migrate/commit/77e06ec1bddb67aa95caf640b05a6fb439f2c1c4))

https://github.com/tox-dev/tox-uv/blob/main/README.md

- Uvx tox@latest -e py -- --with tox-uv
  ([`acb138c`](https://github.com/yhino/pipenv-uv-migrate/commit/acb138c23570f42db0a1f98f0231af7d7cc60e04))


## v0.1.1 (2024-12-23)

### :bug:

- :bug: fix script target of pipenv-uv-migrate
  ([`4c41bf8`](https://github.com/yhino/pipenv-uv-migrate/commit/4c41bf8f05537c5d5e698792b51fe6aff9259c3d))

### Other

- :bookmark: v0.1.1
  ([`d0fa7ce`](https://github.com/yhino/pipenv-uv-migrate/commit/d0fa7ce6a9e5490b2cbe20ebe5d6c2935b9825b3))


## v0.1.0 (2024-12-23)

### :bug:

- :bug: Delete the word "poetry"
  ([`bffcbb0`](https://github.com/yhino/pipenv-uv-migrate/commit/bffcbb08ca9f56192c90b8c65daa00f80ab6e9a2))

- :bug: fix bash option in scripts
  ([`d9ccb01`](https://github.com/yhino/pipenv-uv-migrate/commit/d9ccb014892149619ea2ddc1f1ad99fbcec6ecfc))

- :bug: fixed to not migrate descriptions not supported by uv
  ([`76ca7cc`](https://github.com/yhino/pipenv-uv-migrate/commit/76ca7cc5fa4dc4732f44da80b327baf4d4ad3012))

### :sparkles:

- :sparkles: implement prototype
  ([`2e08dad`](https://github.com/yhino/pipenv-uv-migrate/commit/2e08dad7e7e0a762caf803f1a24d8d0529d54a15))

### Other

- :bookmark: v0.1.0
  ([`1620bd5`](https://github.com/yhino/pipenv-uv-migrate/commit/1620bd5ed85c0bc67db27a0b5fc2102be32191c7))

- :construction_worker: add github actions settings
  ([`30373e3`](https://github.com/yhino/pipenv-uv-migrate/commit/30373e328cf3805362e3b4c5e07bbbe7abfe81c1))

- :green_heart: fix snyk scan workflow
  ([`d2c0ebd`](https://github.com/yhino/pipenv-uv-migrate/commit/d2c0ebd6bfc34c1eda3f0167b9d635cc71911030))

- :green_heart: fix to use uv instead of poetry
  ([`e5a0644`](https://github.com/yhino/pipenv-uv-migrate/commit/e5a06441428aecd1e549566040610472a1782e8e))

- :pencil: add README.md
  ([`a74ec1c`](https://github.com/yhino/pipenv-uv-migrate/commit/a74ec1c52b84dc5a0e4eec9735e0d8f7c8feafe5))

- :pencil: fix badge of codecov
  ([`84f49a0`](https://github.com/yhino/pipenv-uv-migrate/commit/84f49a09a5720427b766c7d8f7138c990981b415))

- :pencil: fix note writing style
  ([`0652332`](https://github.com/yhino/pipenv-uv-migrate/commit/0652332c5c41cdc00dc9fa0fc75d32063e553a10))

- :rotating_light: fix linter warning
  ([`6c01cf2`](https://github.com/yhino/pipenv-uv-migrate/commit/6c01cf2e58c2fe9c9aa52421b5a781f1a2849a90))

- :white_check_mark: add package version test
  ([`481023a`](https://github.com/yhino/pipenv-uv-migrate/commit/481023a2ca834c8bfbf02c2c88c5c6c6b67cf37d))

- :white_check_mark: add unit test code
  ([`02cc26c`](https://github.com/yhino/pipenv-uv-migrate/commit/02cc26c70883aef274a4888141aa732d6a95a07e))

- :wrench: use dev-dependencies instead of uvx
  ([`398d228`](https://github.com/yhino/pipenv-uv-migrate/commit/398d228c5a420d6ef434f09e34b2f7ffbe2068dc))

- Init
  ([`77097f6`](https://github.com/yhino/pipenv-uv-migrate/commit/77097f6d709b50e87830379cbc3d6c19ba2d9c89))
