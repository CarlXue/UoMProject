json.array!(@products) do |product|
  json.extract! product, :id, :product_id, :product_name, :product_description, :product_brand, :product_standard, :cost_aud, :cost_rmb, :unit_price_aud, :unit_price_rmb, :margin_aud, :margin_rmb, :stock_au, :stock_cn
  json.url product_url(product, format: :json)
end
