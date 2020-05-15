#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2019-2020 Mohamad Janati (freaking stupid, right? :|)

import json
from anki.stats import CollectionStats
from anki import version
anki_version = int(version.replace('.', ''))

if anki_version > 2119:
    from aqt.theme import theme_manager


def _graph_mod(self, id, data, conf=None,
           type="bars", xunit=1, ylabel=_("Cards"), ylabel2=""):
    if conf is None:
        conf = {}
    color = "#fff"
    if anki_version > 2119:
        if theme_manager.night_mode:
            color = "#272828"
    # display settings
    if type == "pie":
        conf['legend'] = {'container': "#%sLegend" % id, 'noColumns':2}
    else:
        conf['legend'] = {'container': "#%sLegend" % id, 'noColumns':10}
    conf['series'] = dict(stack=True)
    if not 'yaxis' in conf:
        conf['yaxis'] = {}
    conf['yaxis']['labelWidth'] = 40
    if 'xaxis' not in conf:
        conf['xaxis'] = {}
    if xunit is None:
        conf['timeTicks'] = False
    else:
        #T: abbreviation of day
        d = _("d")
        #T: abbreviation of week
        w = _("w")
        #T: abbreviation of month
        mo = _("mo")
        conf['timeTicks'] = {1: d, 7: w, 31: mo}[xunit]
    # types
    width = self.width
    height = self.height
    if type == "bars":
        conf['series']['bars'] = dict(
            show=True, barWidth=0.8, align="center", fill=0.7, lineWidth=0)
    elif type == "barsLine":
        print("deprecated - use 'bars' instead")
        conf['series']['bars'] = dict(
            show=True, barWidth=0.8, align="center", fill=0.7, lineWidth=3)
    elif type == "fill":
        conf['series']['lines'] = dict(show=True, fill=True)
    elif type == "pie":
        width /= 2.3
        height *= 1.5
        ylabel = ""
        conf['series']['pie'] = dict(
            show=True,
            radius=1,
            stroke=dict(color="%s" % color, width=5),
            label=dict(
                show=True,
                radius=0.8,
                threshold=0.01,
                background=dict(
                    opacity=0.5,
                    color="#000"
                )))
    return (
"""
<table cellpadding=0 cellspacing=10>
<tr>

<td><div style="width: 150px; text-align: center; position:absolute;
 -webkit-transform: rotate(-90deg) translateY(-85px);
font-weight: bold;
">%(ylab)s</div></td>

<td>
<center><div id=%(id)sLegend></div></center>
<div id="%(id)s" style="width:%(w)spx; height:%(h)spx;"></div>
</td>

<td><div style="width: 150px; text-align: center; position:absolute;
 -webkit-transform: rotate(90deg) translateY(65px);
font-weight: bold;
">%(ylab2)s</div></td>

</tr></table>
<script>
$(function () {
    var conf = %(conf)s;
    if (conf.timeTicks) {
        conf.xaxis.tickFormatter = function (val, axis) {
            return val.toFixed(0)+conf.timeTicks;
        }
    }
    conf.yaxis.minTickSize = 1;
    // prevent ticks from having decimals (use whole numbers instead)
    conf.yaxis.tickDecimals = 0;
    conf.yaxis.tickFormatter = function (val, axis) {
            // Just in case we get ticks with decimals, render to one decimal position.  If it's
            // a whole number then render without any decimal (i.e. without the trailing .0).
            return val === Math.round(val) ? val.toFixed(0) : val.toFixed(1);
    }
    if (conf.series.pie) {
        conf.series.pie.label.formatter = function(label, series){
            return '<div class=pielabel>'+Math.round(series.percent)+'%%</div>';
        };
    }
    $.plot($("#%(id)s"), %(data)s, conf);
});
</script>""" % dict(
    id=id, w=width, h=height,
    ylab=ylabel, ylab2=ylabel2,
    data=json.dumps(data), conf=json.dumps(conf)))

CollectionStats._graph = _graph_mod
