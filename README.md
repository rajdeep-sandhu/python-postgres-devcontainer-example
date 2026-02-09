# Python PostgreSQL DevContainer Example

## Set up Python and PostgreSQL DevContainers

- `devcontiainer.json`
  - Refers to `docker-compose.yml` instead of an image.
- `docker-compose.yml`
  - The environment variables are made available to both the `app` and the `db` services.
  - Use a local `.env` file which should not be committed. (See `,env.example`).
    - Environment variables are imported implicitly from it, if this is available.
    - If not, `environment:` uses variables available from the environment. This enables using CodeSpace secrets.
      - These are set up via **Repository | Settings | Secrets and variables**
    - `env_file:` is not specified because, if an actual `.env` file is not present in the ropository, the container build will crash with a file not found error. In this case, it does not automatically default to `environment:`.
    - Mount the volume at `/var/lib/postgresql` for PostgreSQL 18, not of `/var/lib/postgresql/data` (previous versions).

## Caveats

- The storage volume is present only as long as the CodeSpace is not deleted. It persists between CodeSpace runs.
- Therefore, enable database seeding or migration with a minimal dataset required for development and testing. This provides a known starting point.
- The database is initialised with the credentials provided on the first successful DevContainer creation.
  - Rebuilding the CodeSpace after changing the supplied credentials does not change these for the database. Create a new CodeSpace in this case.
  - When running the DevContainers locally, changing the credentials will require removing the volume first.
  
    ```bash
    docker volume list

    docker volume rm <volume_name>
    ```
