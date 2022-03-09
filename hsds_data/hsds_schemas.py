import pandera as pa

hsds_organization_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each organization must have a unique identifier.",
            required=True,
            unique=True,
        ),
        "name": pa.Column(
            dtype="string",
            description="The official or public name of the organization.",
            required=True,
        ),
        "alternate_name": pa.Column(
            dtype="string",
            description="Alternative or commonly used name for the organization.",
            required=False,
        ),
        "description": pa.Column(
            dtype="string",
            description="A brief summary about the organization. It can contain markup such as HTML or Markdown.",
            required=False,
        ),
        "email": pa.Column(
            dtype="string",
            description="The contact e-mail address for the organization.",
            required=False,
        ),
        "url": pa.Column(
            dtype="string",
            description="format: url. The URL (website address) of the organization.",
            required=False,
        ),
        "tax_status": pa.Column(
            dtype="string",
            description="Government assigned tax designation for tax-exempt organizations.",
            required=False,
        ),
        "tax_id": pa.Column(
            dtype="string",
            description="A government issued identifier used for the purpose of tax administration.",
            required=False,
        ),
        "year_incorporated": pa.Column(
            dtype="string",
            description="format: %Y. The year in which the organization was legally formed.",
            required=False,
        ),
        "legal_status": pa.Column(
            dtype="string",
            description="The legal status defines the conditions that an organization is operating under; e.g. non-profit, private corporation or a government organization.",
            required=False,
        ),
    }
)
hsds_program_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each program must have a unique identifier.",
            required=True,
            unique=True,
        ),
        "organization_id": pa.Column(
            dtype="string",
            description="format: uuid. Each program must belong to a single organization. The identifier of the organization should be given here.",
            required=True,
        ),
        "name": pa.Column(
            dtype="string",
            description="The name of the program",
            required=True,
        ),
        "alternate_name": pa.Column(
            dtype="string",
            description="An alternative name for the program",
            required=False,
        ),
    }
)
hsds_service_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each service must have a unique identifier.",
            required=True,
            unique=True,
        ),
        "organization_id": pa.Column(
            dtype="string",
            description="The identifier of the organization that provides this service.",
            required=False,
        ),
        "program_id": pa.Column(
            dtype="string",
            description="The identifier of the program this service is delivered under.",
            required=False,
        ),
        "name": pa.Column(
            dtype="string",
            description="The official or public name of the service.",
            required=False,
        ),
        "alternate_name": pa.Column(
            dtype="string",
            description="Alternative or commonly used name for a service.",
            required=False,
        ),
        "description": pa.Column(
            dtype="string",
            description="A description of the service.",
            required=False,
        ),
        "url": pa.Column(
            dtype="string",
            description="format: url. URL of the service",
            required=False,
        ),
        "email": pa.Column(
            dtype="string",
            description="Email address for the service",
            required=False,
        ),
        "status": pa.Column(
            dtype="string",
            description="The current status of the service.",
            required=True,
        ),
        "interpretation_services": pa.Column(
            dtype="string",
            description="A description of any interpretation services available for accessing this service.",
            required=False,
        ),
        "application_process": pa.Column(
            dtype="string",
            description="The steps needed to access the service.",
            required=False,
        ),
        "wait_time": pa.Column(
            dtype="string",
            description="Time a client may expect to wait before receiving a service.",
            required=False,
        ),
        "fees": pa.Column(
            dtype="string",
            description="Details of any charges for service users to access this service.",
            required=False,
        ),
        "accreditations": pa.Column(
            dtype="string",
            description="Details of any accreditations. Accreditation is the formal evaluation of an organization or program against best practice standards set by an accrediting organization.",
            required=False,
        ),
        "licenses": pa.Column(
            dtype="string",
            description="An organization may have a license issued by a government entity to operate legally. A list of any such licenses can be provided here.",
            required=False,
        ),
        "taxonomy_ids": pa.Column(
            dtype="string",
            description="(Deprecated) A comma separated list of identifiers from the taxonomy table. This field is deprecated in favour of using the service_taxonomy table.",
            required=False,
        ),
    }
)
hsds_service_taxonomy_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each service must have a unique identifier.",
            required=True,
            unique=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service at a given location.",
            required=True,
        ),
        "taxonomy_id": pa.Column(
            dtype="string",
            description="The identifier of this classification from the taxonomy table.",
            required=True,
        ),
        "taxonomy_detail": pa.Column(
            dtype="string",
            description="For advanced uses, this field can indicate a constraint on this classification, using * to combine two taxonomy terms. For example: 'Food Pantry*Homeless' (where 'Food Pantry' and 'Homeless' are identifiers in the taxonomy table) to indicate a food pantry service for homeless clients, but not available to other client groups. In this example, there would be two entries in service_taxonomy, one with 'Food Pantry' and one for 'Homeless' in the taxonomy_id field, but both with the same 'Food Pantry*Homeless' value in the taxonomy_detail field.",
            required=False,
        ),
    }
)
hsds_service_at_location_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier.",
            required=True,
            unique=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service at a given location.",
            required=True,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location where this service operates.",
            required=True,
        ),
        "description": pa.Column(
            dtype="string",
            description="Any additional information that should be displayed to users about the service at this specific location.",
            required=False,
        ),
    }
)
hsds_location_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each location must have a unique identifier",
            required=True,
        ),
        "organization_id": pa.Column(
            dtype="string",
            description="Each location entry should be linked to a single organization. This is the organization that is responsible for maintaining information about this location. The identifier of the organization should be given here. Details of the services the organisation delivers at this location should be provided in the services_at_location table.",
            required=False,
        ),
        "name": pa.Column(
            dtype="string",
            description="The name of the location",
            required=False,
        ),
        "alternate_name": pa.Column(
            dtype="string",
            description="An alternative name for the location",
            required=False,
        ),
        "description": pa.Column(
            dtype="string",
            description="A description of this location.",
            required=False,
        ),
        "transportation": pa.Column(
            dtype="string",
            description="A description of the access to public or private transportation to and from the location.",
            required=False,
        ),
        "latitude": pa.Column(
            dtype="number",
            description="Y coordinate of location expressed in decimal degrees in WGS84 datum.",
            required=False,
        ),
        "longitude": pa.Column(
            dtype="number",
            description="X coordinate of location expressed in decimal degrees in WGS84 datum.",
            required=False,
        ),
    }
)
hsds_phone_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location where this phone number is located",
            required=False,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this is the phone number",
            required=False,
        ),
        "organization_id": pa.Column(
            dtype="string",
            description="The identifier of the organisation for which this is the phone number",
            required=False,
        ),
        "contact_id": pa.Column(
            dtype="string",
            description="The identifier of the contact for which this is the phone number",
            required=False,
        ),
        "service_at_location_id": pa.Column(
            dtype="string",
            description="The identifier of the 'service at location' table entry, when this phone number is specific to a service in a particular location.",
            required=False,
        ),
        "number": pa.Column(
            dtype="string",
            description="The phone number",
            required=False,
        ),
        "extension": pa.Column(
            dtype="number",
            description="The extension of the phone number",
            required=False,
        ),
        "type": pa.Column(
            dtype="string",
            description="Indicates the type of phone service, drawing from the RFC6350 list of types (text (for SMS), voice, fax, cell, video, pager, textphone).",
            required=False,
        ),
        "language": pa.Column(
            dtype="string",
            description="A comma separated list of ISO 639-1, or ISO 639-2 [language codes](available at http://www.loc.gov/standards/iso639-2/php/code_list.php) to represent the languages available from this phone service. The three-letter codes from ISO 639-2 provide greater accuracy when describing variants of languages, which may be relevant to particular communities.",
            required=False,
        ),
        "description": pa.Column(
            dtype="string",
            description="A description providing extra information about the phone service (e.g. any special arrangements for accessing, or details of availability at particular times.",
            required=False,
        ),
        "department": pa.Column(
            dtype="string",
            description="(Deprecated) The department for which this is the phone number. This field is deprecated and will be removed in a future version of HSDS.",
            required=False,
        ),
    }
)
hsds_contact_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each contact must have a unique identifier",
            required=True,
        ),
        "organization_id": pa.Column(
            dtype="string",
            description="The identifier of the organization for which this is a contact",
            required=False,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this is a contact",
            required=False,
        ),
        "service_at_location_id": pa.Column(
            dtype="string",
            description="The identifier of the 'service at location' table entry, when this contact is specific to a service in a particular location.",
            required=False,
        ),
        "name": pa.Column(
            dtype="string",
            description="The name of the person",
            required=False,
        ),
        "title": pa.Column(
            dtype="string",
            description="The job title of the person",
            required=False,
        ),
        "department": pa.Column(
            dtype="string",
            description="The department that the person is part of",
            required=False,
        ),
        "email": pa.Column(
            dtype="string",
            description="format: email. The email address of the person",
            required=False,
        ),
    }
)
hsds_physical_address_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each physical address must have a unique identifier.",
            required=True,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location for which this is the address.",
            required=False,
        ),
        "attention": pa.Column(
            dtype="string",
            description="The person or entity whose attention should be sought at the location (Often included as 'care of' component of an address.)",
            required=False,
        ),
        "address_1": pa.Column(
            dtype="string",
            description="The first line(s) of the address, including office, building number and street.",
            required=False,
        ),
        "address_2": pa.Column(
            dtype="string",
            description="(Deprecated) A second (additional) line of address information. (This field is deprecated: we recommend including all address information before 'city' as a comma separated list in address_1. There is no guarantee that systems will read this line of address information.)",
            required=False,
        ),
        "address_3": pa.Column(
            dtype="string",
            description="(Deprecated) A third (additional) line of address information. (This field is deprecated: we recommend including all address information before 'city' as a comma separated list in address_1. There is no guarantee that systems will read this line of address information.)",
            required=False,
        ),
        "address_4": pa.Column(
            dtype="string",
            description="(Deprecated) The fourth (additional) line of address information. (This field is deprecated: we recommend including all address information before 'city' as a comma separated list in address_1. There is no guarantee that systems will read this line of address information.)",
            required=False,
        ),
        "city": pa.Column(
            dtype="string",
            description="The city in which the address is located.",
            required=False,
        ),
        "region": pa.Column(
            dtype="string",
            description="The region in which the address is located (optional).",
            required=False,
        ),
        "state_province": pa.Column(
            dtype="string",
            description="The state or province in which the address is located.",
            required=False,
        ),
        "postal_code": pa.Column(
            dtype="string",
            description="The postal code for the address.",
            required=False,
        ),
        "country": pa.Column(
            dtype="string",
            description="The country in which the address is located. This should be given as an ISO 3361-1 country code (two letter abbreviation).",
            required=True,
        ),
    }
)
hsds_postal_address_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each postal address must have a unique identifier",
            required=True,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location for which this is the postal address.",
            required=False,
        ),
        "attention": pa.Column(
            dtype="string",
            description="The person or entity whose attention should be sought at the location (Often included as 'care of' component of an address.)",
            required=False,
        ),
        "address_1": pa.Column(
            dtype="string",
            description="The first line(s) of the address, including office, building number and street.",
            required=True,
        ),
        "address_2": pa.Column(
            dtype="string",
            description="(Deprecated) A second (additional) line of address information. (This field is deprecated: we recommend including all address information before 'city' as a comma separated list in address_1. There is no guarantee that systems will read this line of address information.)",
            required=False,
        ),
        "address_3": pa.Column(
            dtype="string",
            description="(Deprecated) A third (additional) line of address information. (This field is deprecated: we recommend including all address information before 'city' as a comma separated list in address_1. There is no guarantee that systems will read this line of address information.)",
            required=False,
        ),
        "address_4": pa.Column(
            dtype="string",
            description="(Deprecated) The fourth (additional) line of address information. (This field is deprecated: we recommend including all address information before 'city' as a comma separated list in address_1. There is no guarantee that systems will read this line of address information.)",
            required=False,
        ),
        "city": pa.Column(
            dtype="string",
            description="The city in which the address is located.",
            required=True,
        ),
        "region": pa.Column(
            dtype="string",
            description="The region in which the address is located (optional).",
            required=False,
        ),
        "state_province": pa.Column(
            dtype="string",
            description="The state or province in which the address is located.",
            required=True,
        ),
        "postal_code": pa.Column(
            dtype="string",
            description="The postal code for the address.",
            required=True,
        ),
        "country": pa.Column(
            dtype="string",
            description="The country in which the address is located. This should be given as an ISO 3361-1 country code (two letter abbreviation)",
            required=True,
        ),
    }
)
hsds_regular_schedule_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this is the regular schedule",
            required=False,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location for which this is the regular schedule",
            required=False,
        ),
        "service_at_location_id": pa.Column(
            dtype="string",
            description="The identifier of the 'service at location' table entry, when this schedule is specific to a service in a particular location.",
            required=False,
        ),
        "weekday": pa.Column(
            dtype="string",
            description="The day of the week that this entry relates to",
            required=False,
        ),
        "opens_at": pa.Column(
            dtype="string",
            description="The time when a service or location opens. This should use HH:MM format and should include timezone information, either adding the suffix 'Z' when the date is in UTC, or including an offset from UTC (e.g. 09:00-05:00 for 9am East Coast Time. ",
            required=False,
        ),
        "closes_at": pa.Column(
            dtype="string",
            description="The time when a service or location opens. This should use HH:MM format and should include timezone information, either adding the suffix 'Z' when the date is in UTC, or including an offset from UTC (e.g. 09:00-05:00 for 9am East Coast Time.",
            required=False,
        ),
    }
)
hsds_holiday_schedule_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this is the holiday schedule",
            required=False,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location for which this is the holiday schedule",
            required=False,
        ),
        "service_at_location_id": pa.Column(
            dtype="string",
            description="The identifier of the 'service at location' table entry, when this schedule is specific to a service in a particular location.",
            required=False,
        ),
        "closed": pa.Column(
            dtype="boolean",
            description="Indicates if a service or location is closed during a public holiday",
            required=True,
        ),
        "opens_at": pa.Column(
            dtype="time",
            description="The time when a service or location opens. This should use HH:MM format and should include timezone information, either adding the suffix 'Z' when the date is in UTC, or including an offset from UTC (e.g. 09:00-05:00 for 9am East Coast Time.",
            required=False,
        ),
        "closes_at": pa.Column(
            dtype="time",
            description="The time when a service or location closes. This should use HH:MM format and should include timezone information, either adding the suffix 'Z' when the date is in UTC, or including an offset from UTC (e.g. 09:00-05:00 for 9am East Coast Time.",
            required=False,
        ),
        "start_date": pa.Column(
            dtype="date",
            description="The first day that a service or location is closed during a public or private holiday",
            required=True,
        ),
        "end_date": pa.Column(
            dtype="date",
            description="The last day that a service or location is closed during a public or private holiday",
            required=True,
        ),
    }
)
hsds_funding_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "organization_id": pa.Column(
            dtype="string",
            description="The identifier of the organization in receipt of this funding.",
            required=False,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service in receipt of this funding",
            required=False,
        ),
        "source": pa.Column(
            dtype="string",
            description="A free text description of the source of funds for this organization or service.",
            required=False,
        ),
    }
)
hsds_eligibility_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this entry describes the eligibility criteria",
            required=False,
        ),
        "eligibility": pa.Column(
            dtype="string",
            description="The rules or guidelines that determine who can receive the service.",
            required=False,
        ),
    }
)
hsds_service_area_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each service area must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this entry describes the service area",
            required=False,
        ),
        "service_area": pa.Column(
            dtype="string",
            description="The geographic area where a service is available. This is a free-text description, and so may be precise or indefinite as necessary.",
            required=False,
        ),
        "description": pa.Column(
            dtype="string",
            description="A more detailed description of this service area. Used to provide any additional information that cannot be communicated using the structured area and geometry fields.",
            required=False,
        ),
    }
)
hsds_required_document_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each document must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which this entry describes the required document",
            required=False,
        ),
        "document": pa.Column(
            dtype="string",
            description="The document required to apply for or receive the service. e.g. 'Government-issued ID', 'EU Passport'",
            required=False,
        ),
    }
)
hsds_payment_accepted_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the services for which the entry describes the accepted payment methods",
            required=False,
        ),
        "payment": pa.Column(
            dtype="string",
            description="The methods of payment accepted for the service",
            required=False,
        ),
    }
)
hsds_language_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each language must have a unique identifier",
            required=True,
        ),
        "service_id": pa.Column(
            dtype="string",
            description="The identifier of the service for which the entry describes the languages in which services are delivered",
            required=False,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location for which the entry describes the languages in which services are delivered",
            required=False,
        ),
        "language": pa.Column(
            dtype="string",
            description="Languages, other than English, in which the service is delivered. Languages are listed as ISO639-1 codes.",
            required=False,
        ),
    }
)
hsds_accessibility_for_disabilities_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "location_id": pa.Column(
            dtype="string",
            description="The identifier of the location for which the entry describes the accessibility provision",
            required=False,
        ),
        "accessibility": pa.Column(
            dtype="string",
            description="Description of assistance or infrastructure that facilitate access to clients with disabilities.",
            required=False,
        ),
        "details": pa.Column(
            dtype="string",
            description="Any further details relating to the relevant accessibility arrangements at this location. E.g. whether advance notice is required to use an accessibility facility.",
            required=False,
        ),
    }
)
hsds_taxonomy_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each taxonomy entry must have a unique identifier. If combining multiple taxonomies with overlapping identifiers, use a prefix to distinguish them.",
            required=True,
            unique=True,
        ),
        "name": pa.Column(
            dtype="string",
            description="The name of this taxonomy term or category.",
            required=True,
        ),
        "parent_id": pa.Column(
            dtype="string",
            description="If this is a child category in a hierarchical taxonomy, give the identifier of the parent category. For top-level categories, this should be left blank.",
            required=False,
        ),
        "parent_name": pa.Column(
            dtype="string",
            description="If this is a child category in a hierarchical taxonomy, give the name of the parent category. For top-level categories, this should be left blank.",
            required=False,
        ),
        "vocabulary": pa.Column(
            dtype="string",
            description="If this is an established taxonomy, detail which taxonomy is in use. For example, AIRS or Open Eligibility.",
            required=False,
        ),
    }
)
hsds_metadata_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "resource_id": pa.Column(
            dtype="string",
            description="Each service, program. location, address, or contact will have a unique identifier. Unique ids are UUIDs.",
            required=True,
        ),
        "last_action_date": pa.Column(
            dtype="datetime",
            description="The date when data was changed.",
            required=True,
        ),
        "last_action_type": pa.Column(
            dtype="string",
            description="The kind of change made to the data; eg create, update, delete",
            required=True,
        ),
        "field_name": pa.Column(
            dtype="string",
            description="The name of field that has been modified",
            required=True,
        ),
        "previous_value": pa.Column(
            dtype="string",
            description="The previous value of a field that has been updated",
            required=True,
        ),
        "replacement_value": pa.Column(
            dtype="string",
            description="The new value of a field that has been updated",
            required=True,
        ),
        "updated_by": pa.Column(
            dtype="string",
            description="The name of the person who updated a value",
            required=True,
        ),
    }
)
hsds_meta_table_description_schema = pa.DataFrameSchema(
    {
        "id": pa.Column(
            dtype="string",
            description="Each entry must have a unique identifier",
            required=True,
        ),
        "name": pa.Column(
            dtype="string",
            description="",
            required=False,
        ),
        "language": pa.Column(
            dtype="string",
            description="",
            required=False,
        ),
        "character_set": pa.Column(
            dtype="string",
            description="",
            required=False,
        ),
    }
)


HSDS_SCHEMAS = {
    "organization_schema": hsds_organization_schema,
    "program_schema": hsds_program_schema,
    "service_schema": hsds_service_schema,
    "service_taxonomy_schema": hsds_service_taxonomy_schema,
    "service_at_location_schema": hsds_service_at_location_schema,
    "location_schema": hsds_location_schema,
    "phone_schema": hsds_phone_schema,
    "contact_schema": hsds_contact_schema,
    "physical_address_schema": hsds_physical_address_schema,
    "postal_address_schema": hsds_postal_address_schema,
    "regular_schedule_schema": hsds_regular_schedule_schema,
    "holiday_schedule_schema": hsds_holiday_schedule_schema,
    "funding_schema": hsds_funding_schema,
    "eligibility_schema": hsds_eligibility_schema,
    "service_area_schema": hsds_service_area_schema,
    "required_document_schema": hsds_required_document_schema,
    "payment_accepted_schema": hsds_payment_accepted_schema,
    "language_schema": hsds_language_schema,
    "accessibility_for_disabilities_schema": hsds_accessibility_for_disabilities_schema,
    "taxonomy_schema": hsds_taxonomy_schema,
    "metadata_schema": hsds_metadata_schema,
    "meta_table_description_schema": hsds_meta_table_description_schema,
}
