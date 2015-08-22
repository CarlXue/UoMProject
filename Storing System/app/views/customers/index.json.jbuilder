json.array!(@customers) do |customer|
  json.extract! customer, :id, :customer_id, :customer_firstName, :customer_lastName, :customer_relationship, :street_number, :street_name, :district, :province, :postcode, :mobile_number, :age_group, :gender, :has_child, :child_age_group
  json.url customer_url(customer, format: :json)
end
