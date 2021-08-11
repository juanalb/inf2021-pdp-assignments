orders = LOAD '/diplomacy/orders.csv'  
USING PigStorage(',') 
AS (game_id:chararray,
    unit_id:chararray,
    unit_order:chararray,
    location:chararray,
    target:chararray,
    target_dest:chararray,
    success:chararray,
    reason:chararray,
    turn_num:chararray);

orders_filtered_by_holland = FILTER orders BY target == '"Holland"';

orders_grouped_by_location = GROUP orders_filtered_by_holland BY (location, target);
orders_count = FOREACH orders_grouped_by_location GENERATE FLATTEN (group) AS (location, target), COUNT($1);

orders_ordered = ORDER orders_count_new BY location ASC;

DUMP orders_ordered;
