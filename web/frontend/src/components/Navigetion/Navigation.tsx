import { Button, Drawer, Tooltip } from "antd"
import React, { useState } from "react"
import { MenuOutlined } from "@ant-design/icons"
import { Link } from "react-router-dom"

function Navigation() {
  const [open, setOpen] = useState(false)

  const showDrawer = () => {
    setOpen(true)
  }

  const onClose = () => {
    setOpen(false)
  }

  return (
    <div className="ml-[20px]">
      <Tooltip title="search">
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
          <Button type="primary" className="w-full bg-black">
            Все файлы
          </Button>
        </Link>
        <p>Some contents...</p>
        <p>Some contents...</p>
      </Drawer>
    </div>
  )
}

export default Navigation
