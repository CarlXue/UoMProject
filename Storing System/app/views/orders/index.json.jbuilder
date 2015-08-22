json.array!(@orders) do |order|
  json.extract! order, :id, :order_id, :customer_id, :product_id, :product_quantity, :order_date, :delivery_fee_rmb, :discount, :unit_price_rmb, :total_cost_rmb, :total_price_rmb
  json.url order_url(order, format: :json)
end
