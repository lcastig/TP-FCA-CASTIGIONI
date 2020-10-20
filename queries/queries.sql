-- mayores goleadas de argentina de local
select m.date, t.name as local, m.homeScore, ta.name as visit, m.awayScore
from futbolStats.match m
inner join futbolStats.team t
on m.homeTeamId = t.id
inner join futbolStats.team ta
on m.awayTeamId = ta.id
where t.name = 'Argentina'
order by homeScore desc
limit 10


-- ultimos diez encuentros entre argentina y brasil
select * from (
select m.date as matchDate, t.name as local, m.homeScore as hsc, ta.name as visit, m.awayScore as asco
from futbolStats.match m
inner join futbolStats.team t
on m.homeTeamId = t.id
inner join futbolStats.team ta
on m.awayTeamId = ta.id
where t.name = 'Argentina'
and ta.name = 'Brazil'
union
select m.date as matchDate, t.name as local, m.homeScore as hsc, ta.name as visit, m.awayScore as asco
from futbolStats.match m
inner join futbolStats.team t
on m.homeTeamId = t.id
inner join futbolStats.team ta
on m.awayTeamId = ta.id
where ta.name = 'Argentina'
and t.name = 'Brazil'
) a order by a.matchDate desc
limit 10
