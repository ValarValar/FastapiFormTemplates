from core.config import get_settings
from utils.db_service import get_mongodb_service
from utils.form_templates import all_templates

settings = get_settings()
mongodb_service = get_mongodb_service(settings.MONGODB_DOCKER_URL)


def main():
    mongodb_service.insert_templates(all_templates)


if __name__ == "__main__":
    main()
