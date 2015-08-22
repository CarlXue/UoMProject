class AddOrderToProduct < ActiveRecord::Migration
  def change
    add_foreign_key :order, :product
  end
end
