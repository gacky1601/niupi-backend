from sqlalchemy.orm import Session

from .districts import districts
from app.api.counties.models import County
from app.api.districts.models import District


def initialize_county_table(database: Session):
    counties = [County(id=index, name=county) for index, county in enumerate(districts)]
    database.bulk_save_objects(counties)


def initialize_district_table(database: Session):
    all_districts = []
    number_of_districts = 0

    for county_index, county in enumerate(districts):
        for district in districts[county]:
            new_district = District(
                id=number_of_districts,
                county_id=county_index,
                name=district
            )

            all_districts.append(new_district)
            number_of_districts += 1

    database.bulk_save_objects(all_districts)
