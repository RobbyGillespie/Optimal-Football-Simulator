"""
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_41.000">15:00</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >KAN 35</td><td class="left " data-stat="detail" ><a name="pbp_41.000"></a><a href="/players/B/ButkHa00.htm">Harrison Butker</a> kicks off 68 yards, returned by <a href="/players/M/MickJa01.htm">Jaydon Mickens</a> for 26 yards (tackle by <a href="/players/O/ODanDo00.htm">Dorian O'Daniel</a>)</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.480</td></tr>

"""
import re
import util
import bs4
import queue
import json
import sys
import csv

link = "https://www.pro-football-reference.com/boxscores/202102070tam.htm"

request_obj = util.get_request(link)
document = util.read_request(request_obj)
soup = bs4.BeautifulSoup(document, "html5lib")
main_title = tag.find("div", class_="table_container")

#<div class="table_container" id="div_pbp">