with define_afford as(
select *
  ,substr(sold_date, 8) AS year
  ,beds ||' beds '|| property_type as new_type
  ,(case when  price <=  800000 and property_type ='House' then 1 when price <=  500000 and property_type ='ApartmentUnitFlat'  then 1 else 0 end)as affordable
  from properties_cleaned
  where property_type = 'House'  or property_type = 'ApartmentUnitFlat' 
  order by year
), last_5years as (
 select listing_id
	,affordable
  , suburb
  , year
  , new_type
  ,price
 from define_afford
 where price >= 50000 and year >= '2015' and year <= '2021'
), count_total as (
 select listing_id
  , suburb
  , year
  , new_type
  ,price
  ,affordable
  ,row_number() over (PARTITION by suburb, year, new_type order by price) as rn
  ,count(price) over (PARTITION by suburb, year, new_type) as total_num
 from last_5years
), median_count as(
select *
  ,(case when total_num % 2 = 1 then ((total_num + 1) / 2)  else (total_num / 2 + 1) end)as median_row 
   ,sum(affordable) over (PARTITION by suburb, year, new_type) as total_afford
 from count_total
),median_price_and_count_afford as (
 select *
  ,(case when  median_row = rn then price else null end)as median_price
  ,(total_afford*100.0)/(total_num*100.0) * 100.0 as affordability
  from median_count
  where median_price is NOT NULL and total_num >= 10
  group by suburb, year, new_type   
), pre_price as(
select *
  ,lag(price,1) over (PARTITION by suburb, new_type order by year) as pre1_price
  ,lag(price,3) over (PARTITION by suburb, new_type order by year) as pre3_price
  ,lag(price,5) over (PARTITION by suburb, new_type order by year) as pre5_price
  from median_price_and_count_afford
), keep_increase as(
 select suburb
 ,new_type
 ,affordability
 ,price
 ,median_price - pre1_price as pre1_diff
 ,median_price - pre3_price as pre3_diff
 ,median_price - pre5_price as pre5_diff
  from pre_price
  where year ='2021' and pre3_price>= pre5_price and pre1_price>= pre3_price and median_price >= pre1_price
),final as (
SELECT keep_increase.suburb, keep_increase.new_type,keep_increase.affordability,keep_increase.pre1_diff,keep_increase.pre3_diff,keep_increase.pre5_diff,keep_increase.price,start_2016_price_1500000_with_dist_filtered.distance_to_cbd
FROM keep_increase
LEFT JOIN start_2016_price_1500000_with_dist_filtered
ON keep_increase.suburb = start_2016_price_1500000_with_dist_filtered.suburb)

select  * from final;
