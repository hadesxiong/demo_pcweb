// 菜单配置
export const menuMap = [
  {
    menu_key: "dashboard",
    menu_title: "数据看板",
    menu_icon: "icon-dashboard",
    sub_menu: [
      {
        menu_key: "dashboard-main",
        menu_title: "重要指标分析",
        menu_icon: "",
        menu_name: "dashboard-main",
        menu_params: {},
      },
    ],
  },
  {
    menu_key: "rank",
    menu_title: "业绩排行",
    menu_icon: "icon-computer",
    sub_menu: [
      {
        menu_key: "rank-important",
        menu_title: "重要指标排行",
        menu_icon: "",
        menu_name: "rank-important",
        menu_params: {},
      },
    ],
  },
  {
    menu_key: "table",
    menu_title: "数据报表",
    menu_icon: "icon-notes",
    sub_menu: [
      {
        menu_key: "enterprise-table",
        menu_title: "企金数据报表",
        menu_icon: "",
        menu_name: "table-detail",
        menu_params: { table_class: "enterprise" },
      },
      {
        menu_key: "retail-table",
        menu_title: "零售数据报表",
        menu_icon: "",
        menu_name: "table-detail",
        menu_params: { table_class: "retail" },
      },
      {
        menu_key: "bank-table",
        menu_title: "同业数据报表",
        menu_icon: "",
        menu_name: "table-detail",
        menu_params: { table_class: "bank" },
      },
      {
        menu_key: "other-table",
        menu_title: "其他数据报表",
        menu_icon: "",
        menu_name: "table-detail",
        menu_params: { table_class: "other" },
      },
    ],
  },
  {
    menu_key: "settings",
    menu_title: "数据管理",
    menu_icon: "icon-data",
    sub_menu: [
      {
        menu_key: "data-manage",
        menu_title: "数据导入",
        menu_icon: "",
        menu_name: "data-manage",
        menu_params: {},
      },
      {
        menu_key: "org-manage",
        menu_title: "机构管理",
        menu_icon: "",
        menu_name: "org-manage",
        menu_params: {},
      },
      {
        menu_key: "user-manage",
        menu_title: "用户管理",
        menu_icon: "",
        menu_name: "user-manage",
        menu_params: {},
      },
    ],
  },
];
