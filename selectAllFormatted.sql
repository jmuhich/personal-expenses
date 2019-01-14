select
	transactionDate,
	dateProcessed,
	case when withdrawalAmount is null then null else printf("%.2f", withdrawalAmount) end as withdrawalAmount,
	case when depositAmount is null then null else printf("%.2f", depositAmount) end as depositAmount,
	description,
	category,
	paymentMethod,
	account,
	merchantType,
	accountDescription
from expenses
order by transactionDate