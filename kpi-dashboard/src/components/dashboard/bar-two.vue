<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex fd_r jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="font_16 fw_500 fc_l1">{{ bar_data.db_title }}</div>
                <div :class="bar_data.tag_class" class="br_4">{{ bar_data.tag_name }}</div>
            </div>
            <div class="d_flex fai_c jc_fe gap_16">
                <a-dropdown>
                    <a class="d_flex fai_c gap_8 fc_brand6">
                        {{ choose_org }}
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <div v-for="(item, index) in org_filter" :key="index">
                                <a-sub-menu v-if="item.children" :key="item.org_key" :title="item.org_name">
                                    <a-menu-item v-for="sub_item in item.children" :key="sub_item.org_key"
                                        @click="chooseOrg(sub_item)">{{
                                            sub_item.org_name }}</a-menu-item>
                                </a-sub-menu>
                                <a-menu-item v-else @click="chooseOrg(item)">{{ item.org_name }}</a-menu-item>
                            </div>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-date-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false"
                    v-model:value="date_value[1]" @openChange="handlePickerClose">
                    <template #suffixIcon>
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </template>
                </a-date-picker>
            </div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c w_p100">
                <div :style="{ height: db_height, width: db_width }" :id="db_id" class="w_p100 h_p100"></div>
            </div>
        </div>
    </div>
</template>

<style>
.custom_dp {
    padding-left: 0px;
    padding-right: 0px;
}

.custom_dp input {
    color: #165fdd !important;
    width: 55px !important;
}

.custom_dp span {
    padding-left: 0px !important;
    padding-right: 0px !important;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Down } from '@icon-park/vue-next';
import { Dropdown, Menu, SubMenu, MenuItem } from 'ant-design-vue';
import { echartsResize } from '@/utils/echartsResize.js';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/chart/bar';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/grid';

export default defineComponent({
    name: "BarTwo",
    components: {
        'icon-down': Down,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-sub-menu': SubMenu,
        'a-menu-item': MenuItem
    },
    props: {
        db_id: { type: String },
        bar_data: { type: Object },
        org_filter: { type: Object },
        cur_org: { type: String },
        cur_date: { type: Array }
    },
    data() {
        return {
            db_width: "100%",
            db_height: "100%"
        };
    },
    setup(props) {
        const date_value = ref(props.cur_date);
        return {
            date_value,
            selectedKeys: ref([]),
            choose_org: ref(props.cur_org)
        }
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            // console.log(this.id);
            let myChart = echarts.init(document.getElementById(this.db_id));
            myChart.setOption(this.bar_data.db_option);
            //添加自适应
            // window.addEventListener('resize', function () {
            //     myChart.resize();
            // })
            document.getElementById(this.db_id).addEventListener('resize', function () {
                myChart.resize();
            });
            echartsResize(document.getElementById(this.db_id), myChart);
        },
        handlePickerClose(status) {
            if (!status) {
                console.log(this.date_value)
            }
        },
        chooseOrg(item) {
            this.selectedKeys.push(item.org_key);
            this.choose_org = item.org_name;
        }
    }
})
</script>