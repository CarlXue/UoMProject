class CreateCustomers < ActiveRecord::Migration
  def change
    create_table :customers do |t|
      t.integer :customer_id
      t.text :customer_firstName
      t.text :customer_lastName
      t.text :customer_relationship
      t.text :street_number
      t.text :street_name
      t.text :district
      t.text :province
      t.integer :postcode
      t.integer :mobile_number
      t.text :age_group
      t.text :gender
      t.boolean :has_child
      t.text :child_age_group

      t.timestamps null: false
    end
  end
end
