-- Insert data from Share & Fund into FitDefault

-- ----------------------------------------------------------------------------
-- 1. make the basic table by join Share&Fund -----------------

-- Expectation fetch time: 976 sec

INSERT INTO research_fitdefault (
	Name,
	Category,
	MFVA,
	SubAdvised,
	IndexFund,
	WatchList,
	VIT,
	FundofFunds,
	InceptionDate,
	Advisor,
	Subadvisor,
	AUM,
	NFYTD,
	NF2017,
	NF2016,
	TR_YTD,
	TR_1y,
	TR_2y,
	TR_3y,
	TR_5y,
	TR_10y,
	SubStart,
	SubSched,
	SubAdvEffRate,
	SubRate,
	Alpha,
	ExcessRet,
	Sharpe,
	InfoRat,
	Beta,
	Stdev,
	R2,
	UpsideCap,
	DownsideCap,
	TrackingErr,
	QRK_YTD,
	QRK_1y,
	QRK_2y,
	QRK_3y,
	QRK_5y,
	QRK_10y,
	QRK_15y,
	QRK_Alpha,
	QRK_ExcessRet,
	QRK_Sharpe,
	QRK_InfoRat,
	QRK_Beta,
	QRK_Stdev,
	QRK_R2,
	QRK_UpsideCap,
	QRK_DownsideCap,
	QRK_TrackingErr,
	TeamManaged,
	ProspectusNetExpenseRatio,
	ManagerName,
	ManagerTenureLongest,
	ManagerTenureAverage,
	Benchmark,
    SecId,
	FundId
)
SELECT 
	s.name Name,
	f.MSCat Category,
	f.MFVA MFVA,
	f.SubAdvd SubAdvised,
	f.Indexed IndexFund,
	f.WatchLst WatchList,
	f.VIT VIT,
	f.FoF FundofFunds,
	f.InceptDt InceptionDate,
	f.Advisor Advisor,
	f.SubAdv  Subadvisor,
	f.APAUM AUM,
	f.NFYTD NFYTD,
	f.NF2017 NF2017,
	f.NF2016 NF2016,
	s.TR_YTD TR_YTD,
	s.TR_1Y TR_1y,
	s.TR_2Y TR_2y,
	s.TR_3Y TR_3y,
	s.TR_5Y TR_5y,
	s.TR_10Y TR_10y,
	f.SubStart SubStart,
	f.SubSch SubSched,
	f.SubRateP SubAdvEffRate,
	f.SubRate SubRate,
	s.Alpha3 Alpha,
	s.ExRet3 ExcessRet,
	s.Sharpe3 Sharpe,
	s.InfoRat3 InfoRat,
	s.Beta3 Beta,
	s.Stdev3 Stdev,
	s.R23 R2,
	s.UpCap3 UpsideCap,
	s.DnCap3 DownsideCap,
	s.TrckErr3 TrackingErr,
	f.QKYTD QRK_YTD,
	f.QK1Y QRK_1y,
	f.QK2Y QRK_2y,
	f.QK3Y QRK_3y,
	f.QK5Y QRK_5y,
	f.QK10Y QRK_10y,
	f.QK15Y QRK_15y,
	f.QKAlph3 QRK_Alpha,
	f.QKExRt3 QRK_ExcessRet,
	f.QKShrp3 QRK_Sharpe,
	f.QKInfR3 QRK_InfoRat,
	f.QKBeta3 QRK_Beta,
	f.QKStdv3 QRK_Stdev,
	f.QKRsq3 QRK_R2,
	f.QKUpS3 QRK_UpsideCap,
	f.QKDnS3 QRK_DownsideCap,
	f.QKTrEr3 QRK_TrackingErr,
	f.TeamMgd TeamManaged,
	s.NExpPrs ProspectusNetExpenseRatio,
	f.MgrName ManagerName,
	f.MgrTenL ManagerTenureLongest,
	f.MgrTenA ManagerTenureAverage,
	f.Bench Benchmark,
    s.SecId,
	s.FundId
from research_shares s, research_funds f
where s.secid=f.secid -- and s.fundid=f.fundid
group by 
	Name,
	Category,
	MFVA,
	SubAdvised,
	IndexFund,
	WatchList,
	VIT,
	FundOfFunds,
	InceptionDate,
	Advisor,
	SubAdvisor,
	AUM,
	NFYTD,
	NF2017,
	NF2016,
	TR_YTD,
	TR_1Y,
	TR_2Y,
	TR_3Y,
	TR_5Y,
	TR_10Y,
	SubStart,
	SubSched,
	SubAdvEffRate,
	SubRate,
	Alpha,
	ExcessRet,
	Sharpe,
	InfoRat,
	Beta,
	Stdev,
	R2,
	UpsideCap,
	DownsideCap,
	TrackingErr,
	QRK_YTD,
	QRK_1Y,
	QRK_2Y,
	QRK_3Y,
	QRK_5Y,
	QRK_10Y,
	QRK_15Y,
	QRK_Alpha,
	QRK_ExcessRet,
	QRK_Sharpe,
	QRK_InfoRat,
	QRK_Beta,
	QRK_Stdev,
	QRK_R2,
	QRK_UpsideCap,
	QRK_DownsideCap,
	QRK_TrackingErr,
	TeamManaged,
	ProspectusNetExpenseRatio,
	ManagerName,
	ManagerTenureLongest,
	ManagerTenureAverage,
	Benchmark,
    SecId,
	FundId
;


-- check if success
select AdvisorId_id, CategoryId_id, ManagerNameid_id, SubAdvisorId_id, SecId, FundId from research_fitdefault;




-- ----------------------------------------------------------------------------
-- 2. Insert the section tables for searching ----------------------

-- == insert the Categorys (MSCat) table == -- 
INSERT INTO research_categorys (Name)
select Category AS Name from research_fitdefault 
where Category is not null 
group by Category 
order by Category
;

-- == insert the Advisors (Advisor) table == -- 
INSERT INTO research_advisors (Name)
select Advisor AS Name from research_fitdefault 
where Advisor is not null 
group by Advisor 
order by Advisor
;

-- == insert the SubAdvisors (SubAdv) table == -- 
INSERT INTO research_subadvisors (Name)
select SubAdvisor AS Name from research_fitdefault 
where SubAdvisor is not null 
group by SubAdvisor 
order by SubAdvisor
;

-- == insert the Managernames (MgrName) table == -- 
INSERT INTO research_managernames (Name)
select ManagerName AS Name from research_fitdefault 
where ManagerName is not null 
group by ManagerName 
order by ManagerName
;


-- ----------------------------------------------------------------------------
-- 3. Update IDs from the section tables --------------------------
-- using py in the data sheets folder


