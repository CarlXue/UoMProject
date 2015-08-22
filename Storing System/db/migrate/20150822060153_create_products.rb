class CreateProducts < ActiveRecord::Migration
  def change
    create_table :products do |t|
      t.integer :product_id
      t.text :product_name
      t.text :product_description
      t.text :product_brand
      t.text :product_standard
      t.float :cost_aud
      t.float :cost_rmb
      t.float :unit_price_aud
      t.float :unit_price_rmb
      t.float :margin_aud
      t.float :margin_rmb
      t.integer :stock_au
      t.integer :stock_cn

      t.timestamps null: false
    end
  end
end
