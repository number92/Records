SELECT services.name, services.duration, services.specialization_id, services.id 
FROM services 
WHERE services.id = $1::INTEGER ORDER BY services.id

SELECT specialist_service_associations.service_id AS specialist_service_associations_service_id, specialist_service_associations.price AS specialist_service_associations_price, specialist_service_associations.description AS specialist_service_associations_description, specialist_service_associations.specialist_id AS specialist_service_associations_specialist_id, specialist_service_associations.id AS specialist_service_associations_id, specialists_1.name AS specialists_1_name, specialists_1.middle_name AS specialists_1_middle_name, specialists_1.last_name AS specialists_1_last_name, specialists_1.telegram_id AS specialists_1_telegram_id, specialists_1.phone AS specialists_1_phone, specialists_1.id AS specialists_1_id 
FROM specialist_service_associations LEFT OUTER JOIN specialists AS specialists_1 ON specialists_1.id = specialist_service_associations.specialist_id 
WHERE specialist_service_associations.service_id IN ($1::INTEGER)
