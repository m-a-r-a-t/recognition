import { Button, Drawer, Tooltip } from "antd"
import React, { useState } from "react"
import { MenuOutlined } from "@ant-design/icons"
import { Link } from "react-router-dom"
import { useAppDispatch, useAppSelector } from "../../hook/redux"
import { mainSlice } from "../../store/reducers/MainSlice"

function Navigation() {
  const dispatch = useAppDispatch()
  const { setAllFileSelect } = mainSlice.actions

  const [open, setOpen] = useState(false)

  const showDrawer = () => {
    setOpen(true)
  }

  const onClose = () => {
    setOpen(false)
  }

  return (
    <div className="ml-[20px]">
      <Tooltip title="menu">
        <Button
          shape="circle"
          icon={<MenuOutlined />}
          size="large"
          onClick={showDrawer}
        />
      </Tooltip>
      <Drawer
        title="Меню"
        placement={"left"}
        closable={false}
        onClose={onClose}
        open={open}
        key={"left"}
      >
        <Link to="/allfile/">
          <Button
            type="primary"
            className="w-full text-black border-black"
            onClick={() => {
              dispatch(setAllFileSelect([]))
            }}
          >
            Все файлы
          </Button>
        </Link>
        <Link to="/">
          <Button
            type="primary"
            className="w-full text-black mt-[20px] border-black"
            onClick={() => {
              dispatch(setAllFileSelect([]))
            }}
          >
            Загрузить файлы
          </Button>
        </Link>
      </Drawer>
    </div>
  )
}

export default Navigation
