# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20150822063150) do

  create_table "customers", force: :cascade do |t|
    t.integer  "customer_id"
    t.text     "customer_firstName"
    t.text     "customer_lastName"
    t.text     "customer_relationship"
    t.text     "street_number"
    t.text     "street_name"
    t.text     "district"
    t.text     "province"
    t.integer  "postcode"
    t.integer  "mobile_number"
    t.text     "age_group"
    t.text     "gender"
    t.boolean  "has_child"
    t.text     "child_age_group"
    t.datetime "created_at",            null: false
    t.datetime "updated_at",            null: false
  end

  create_table "orders", force: :cascade do |t|
    t.integer  "order_id"
    t.integer  "customer_id"
    t.integer  "product_id"
    t.integer  "product_quantity"
    t.date     "order_date"
    t.float    "delivery_fee_rmb"
    t.float    "discount"
    t.float    "unit_price_rmb"
    t.float    "total_cost_rmb"
    t.float    "total_price_rmb"
    t.datetime "created_at",       null: false
    t.datetime "updated_at",       null: false
  end

  create_table "products", force: :cascade do |t|
    t.integer  "product_id"
    t.text     "product_name"
    t.text     "product_description"
    t.text     "product_brand"
    t.text     "product_standard"
    t.float    "cost_aud"
    t.float    "cost_rmb"
    t.float    "unit_price_aud"
    t.float    "unit_price_rmb"
    t.float    "margin_aud"
    t.float    "margin_rmb"
    t.integer  "stock_au"
    t.integer  "stock_cn"
    t.datetime "created_at",          null: false
    t.datetime "updated_at",          null: false
  end

end
