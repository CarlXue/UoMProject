class CreateOrders < ActiveRecord::Migration
  def change
    create_table :orders do |t|
      t.integer :order_id
      t.integer :customer_id
      t.integer :product_id
      t.integer :product_quantity
      t.date :order_date
      t.float :delivery_fee_rmb
      t.float :discount
      t.float :unit_price_rmb
      t.float :total_cost_rmb
      t.float :total_price_rmb

      t.timestamps null: false
    end
  end
end
