<template>
    <div class="d_flex fd_c gap_20 h_p100 w_p100">
        <div class="d_flex p_20 bg_white gap_20 fai_c w_p100 jc_sb">
            <a-row :gutter="[20,20]" class="fwrap_n w_p100">
                <a-col :span="4"><menu-input :cp_data="org_option" @menu-select="handleMenuSelect"></menu-input></a-col>
                <a-col :span="4"><menu-input :cp_data="character_option" @menu-select="handleMenuSelect"></menu-input></a-col>
                <a-col :span="4"><menu-input :cp_data="line_option" @menu-select="handleMenuSelect"></menu-input></a-col>
                <a-col :span="8">                
                    <a-input v-model:value='search_form.key_word' placeholder="输入导入人信息或者导入编号进行搜索"
                        class="fai_c bg_l2 br_2  ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no b_n">
                        <template #suffix><icon-search size="14" class="mr_8 lh_1"></icon-search></template>
                    </a-input>
                </a-col>
            </a-row>
            <div class="d_flex gap_20 fai_c">
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="resetSearch">
                    <template #icon><icon-redo size="14" class="mr_8 lh_1"></icon-redo></template>
                    重置
                </a-button>
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmSearch">
                    <template #icon><icon-search size="14" class="mr_8 lh_1"></icon-search></template>
                    查询
                </a-button>
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="showModal">
                    <template #icon><icon-add size="14" class="mr_8 lh_1"></icon-add></template>
                    新增
                </a-button>
            </div>
        </div>
        <div class="d_flex p_20 bg_white gap_20 fd_c h_p100">
            <edit-table :table_obj="table_obj" :status="status" :editable="can_edit" @table-edit="handleTableEdit"></edit-table>
            <div class="d_flex fai_c jc_fe">
                <a-pagination :current="page_obj.current" :total="page_obj.total" :pageSize="page_obj.size"
                    :pageSizeOptions="page_obj.sizeOptions" @change="changePage"
                    @showSizeChange="changeSizeOptions"></a-pagination>
            </div>
        </div>    
    </div>
    <div class="modal_con">
        <modal-input :modal_obj="modal_obj" :visible="visible" @modal-confirm="handleModalConfirm"></modal-input>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Col, Row, Input, Divider, Button, Pagination, message } from 'ant-design-vue';
import { Search as SearchIcon, Redo, AddFour } from '@icon-park/vue-next';

import MenuInput from '@/components/other/menu-input.vue';
import ModalInput from '@/components/other/modal-input.vue';
import EditTable from '@/components/manage/edit-table.vue';

import { api } from '@/utils/commonApi.js';
import { userTableHead, userEditIndex, userEditMap, userSearchInfo, updateUserModal } from '@/assets/config/user-manage.js';

const myApi = api();

export default defineComponent({
    name: 'UserManage',
    components: {
        'menu-input': MenuInput,
        'edit-table': EditTable,
        'modal-input': ModalInput,
        'a-col': Col,
        'a-row': Row,
        'a-input': Input,
        'a-divider': Divider,
        'a-button': Button,
        'a-pagination': Pagination,
        'icon-search': SearchIcon,
        'icon-redo': Redo,
        'icon-add': AddFour
    },
    data() {
        return {}
    },
    setup() {       
        return {
            character_option: ref({menu_data:[{ref_code:0,ref_name:'全部'}],menu_key:{code:'ref_code',label:'ref_name'},select_title:'character_option'}),
            org_option: ref({menu_data:[{ref_code:0,ref_name:'全部'}],menu_key:{code:'ref_code',label:'ref_name'},select_title:'org_option'}),
            line_option: ref({menu_data:[{ref_code:0,ref_name:'全部'}],menu_key:{code:'ref_code',label:'ref_name'},select_title:'line_option'}),
            search_form: ref({
                character_option: {ref_code:0,ref_name:'全部'},
                line_option: {ref_code:0,ref_name:'全部'},
                org_option: {ref_code:0,ref_name:'全部'},
                key_word: ''
            }),
            page_obj: ref({current:1,size:15,total:100,sizeOptions:['15', '30', '60']}),
            table_obj: ref({
                columns: ref(userTableHead),
                data: ref([]),
                editIndex: ref(userEditIndex),
                editMap: ref(userEditMap),
                search_obj: ref(userSearchInfo)
            }),
            status: ref(false),
            can_edit: ref(true),
            modal_obj: ref({title:'新增用户',data:ref(updateUserModal)}),
            visible: ref(false)
        }
    },
    mounted() {
        // 选项初始化赋值
        myApi.get('/api/other/getFilter',{params: {type:'ubg.uc.og'}}).then(
            (response) => {
                this.character_option.menu_data = response.data.data.user_character
                this.org_option.menu_data =  response.data.data.org_group
                this.line_option.menu_data = response.data.data.user_belong_group
            }
        ),
        this.getUserList()
    },
    methods: {
        // 接收menuSelect带来的参数
        handleMenuSelect(value) {
            this.search_form[value.title] = value.data;
        },
        handleTableEdit(value) {
            // console.log(value);
            const post_data = {
                'user': value.notes_id,
                'type': 'update',
                'update_data': {
                    'user_name': value.user_name,
                    'user_character': value.user_character,
                    'user_belong_group': value.user_belong_group,
                    'user_belong_org': value.user_belong_org
                }
            }
            message.loading({content:'提交修改,请稍后...',duration:0,class:'msg_loading'});
            this.can_edit = false;
            myApi.post('/api/user/updateUser',post_data).then(
                (response) => {
                    console.log(response);
                    message.destroy();
                    message.success({content:'修改完成',duration:1.5,class:'msg_loading',onClose:()=>{this.getUserList();}})
                    this.can_edit = true;
                }
            ).catch(
                (response) => {
                    console.log(response);
                    message.destroy();
                    message.error({content:'提交失败...',duration:1.5,class:'msg_loading',onClose:()=>{this.can_edit=true;}})
                }
            )
        },
        async getUserList() {
            // loading 开始
            this.status = true;
            // 主逻辑
            const get_params = {
                line: this.search_form.line_option.ref_code,
                character: this.search_form.character_option.ref_code,
                org: this.search_form.org_option.ref_code,
                client: 0,
                page: this.page_obj.current,
                size: this.page_obj.size,
                ext: this.search_form.key_word
            }
            const user_list = await myApi.get('/api/user/getUserList',{params: get_params})
            // 组装table_obj
            this.table_obj.data = user_list.data.data;
            // 为data添加key
            this.table_obj.data = this.table_obj.data.map((item, index) => { return { ...item, key: index.toString() } });
            this.page_obj.total = user_list.data.data_total
            // 处理editIndex
            this.table_obj.editIndex.find(item=>item.column == 'character_name').option_list = this.character_option.menu_data
            this.table_obj.editIndex.find(item=>item.column == 'group_name').option_list = this.line_option.menu_data
            // 处理editMap的range属性
            this.table_obj.editMap.find(item=>item.name_target == 'character_name').range = this.character_option.menu_data
            this.table_obj.editMap.find(item=>item.name_target == 'group_name').range = this.line_option.menu_data
            // loading 结束
            this.status = false;
        },
        // 展示新增表单
        showModal() {
            this.visible = true
        },
        // 重置查询条件
        resetSearch() {
            this.search_form = {
                character_option: {ref_code:0,ref_name:'全部'},
                line_option: {ref_code:0,ref_name:'全部'},
                org_option: {ref_code:0,ref_name:'全部'},
                key_word: ''
            }
        },
        // 提交查询
        confirmSearch() {
            // console.log(this.search_form);
            this.getUserList();
        },
        // 翻页
        changePage(page) {
            this.page_obj.current = page
            this.getUserList()
        },
        // 设定pageSize
        changeSizeOptions(_, size) {
            // 设定size，页数重置
            this.page_obj.size = size;
            this.$nextTick(()=>{
                this.page_obj.current = 1;
                this.getUserList();
            })
        },
        handleModalConfirm(value) {
            if (value.type == 2) {
                let post_data = {}
                let post_headers = {}
                if (value.data.type == 0) {
                    post_data = {
                        is_multi: false,
                        update_data: {
                            'notes_id': value.data.notes_id,
                            'user_name': value.data.user_name,
                            'user_belong_org': value.data.org_name.key,
                            'user_belong_group': value.data.group_name.ref_code,
                            'user_character': value.data.character_name.ref_code
                        }
                    }
                    post_headers = {'Content-Type': 'application/json'}
                } else if (value.data.type == 1) {
                    post_data = new FormData();
                    post_data.append('is_multi',true);
                    post_data.append('update_file',value.data.upload_file);
                    post_headers = {'Content-Type': 'multipart/form-data'}
                }
                message.loading({content:'正在创建用户,请稍后...',duration:0,class:'msg_loading'})
                myApi.post('/api/user/createUser',post_data,{headers:post_headers}).then(
                    () => {
                        message.destroy();
                        message.success({content:'用户创建完成',duration:1.5,class:'msg_loading',onClose:()=>{this.getUserList()}})
                    }
                ).catch(
                    (response) => {
                        message.destroy();
                        message.error({content:`'用户创建失败,'${response.data.msg}`,duration:2,class:'msg_loading'})
                    }
                )
            }
            this.visible = !this.visible
        }
    }
})
</script>