// Best Time to Buy and Sell Stock II
// Say you have an array for which the ith element is the price of a given stock on day i.

// Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

// Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
// You are here!
// Your runtime beats 92.13 % of golang submissions.
func maxProfit(prices []int) int {
	profit, margin := 0, 0
	hold := false
	if len(prices) < 2 {
		return profit
	}
	if p := prices[0]; p < prices[1] {
		margin = -p
		hold = true
	}
	for i := 1; i < len(prices)-1; i++ {
		p := prices[i]
		if p < prices[i+1] && p <= prices[i-1] && !hold {
			margin = -p
			hold = true
		}
		if hold && p > prices[i+1] && p >= prices[i-1] {
			profit += margin + p
			hold = false
		}
	}
	if p := prices[len(prices)-1]; p >= prices[len(prices)-2] && hold {
		profit += margin + p
	}
	return profit
}
